import sys
import random
import copy
import csv
import numpy as np
import time
from algo_glouton import glouton
from algo_dynamique import dynamique

def readFile(arg): 
    file = open(arg, "r")
    file.readline()
    A = []
    for line in file:
        line = line.strip()
        line = line.replace("\t", ",")
        if len(line) > 0:
            A.append(map(int, line.split(' ')))
    file.close()

    return A[0]
    
def costFromFingers(couts, notes, fingers):
	cout = 0
	for i in range(0, len(fingers)-1):
		cout += couts[notes[i]][fingers[i]][notes[i+1]][fingers[i+1]]
	return cout

def findLowerCost(couts, notes, fingers, firstCost):
	if(len(notes) < 1000 ):
		maxIt = len(notes)
	else:
		maxIt = 1000
	for i in range(0, maxIt):
		index = random.randint(0,len(notes) - 2)
		for d in range(0, 5):
			if(couts[notes[index-1]][fingers[index-1]][notes[index]][fingers[index]] + couts[notes[index]][fingers[index]][notes[index+1]][fingers[index+1]] > couts[notes[index-1]][fingers[index-1]][notes[index]][d] + couts[notes[index]][d][notes[index+1]][fingers[index+1]]):
				fingers[index] = d
	cost = costFromFingers(couts, notes, fingers)
	return [fingers, cost]
			
    
def voisinage(couts, notes):
	start = time.time()
	result = glouton(couts, notes)
	result = findLowerCost(couts, notes, result[0], result[1])
	end = time.time()
	temps = end - start
	result.append(round(temps*1000))
	return result
    
    
def main(argv):
	file = open(argv[1], "r")
	n = file.readline()
	file.close()
	notes = readFile(argv[1])
	load_file = np.loadtxt('cout_transition.txt', dtype=int)
	cout_transition = load_file.reshape((24, 5, 24, 5))
	
	
	
	result = voisinage(cout_transition, notes)
	
	fingers = ''
	for finger in result[0]:
		fingers += str(finger)
		fingers += ' '
	cost = result[1]
	time = result[2]
	
	for arg in argv:
		if arg == "-t":
			print(time)
		if arg == "-p":
			print(cost)
		if arg == "-c":
			print(fingers)
	return
  
if __name__ == "__main__":
    main(sys.argv[1:])
