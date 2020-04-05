import sys
import csv
import numpy as np
import time


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

def indexOfMinValue(table):
	index = 0
	min = table[0]
	for i in range(0, len(table)):
		if table[i] < min:
			index = i
			min = table[i]
	return index

def findFingers(transitions, firstFinger, size):
	fingers = [0 for x in range(size)]
	fingers[0] = firstFinger
	for i in range(1, size):
		fingers[i] = transitions[size-i][fingers[i-1]]
	return fingers

def dynamicTable(couts, notes):
	n = len(notes)
	tc = [[0 for x in range(5)] for x in range(n)]
	
	fingers = [[0 for x in range(5)] for x in range(n)]
	
	for d in range(0, 5): 
		tc[0][d] = 0
		fingers[0][d] = d
	
	for k in range(1, n):
		for d in range(0,5):
			index = 0
			min = couts[notes[n-k-1]][d][notes[n-k]][0] + tc[k-1][0]
			for d_bis in range(0,5):
				if couts[notes[n-k-1]][d][notes[n-k]][d_bis] + tc[k-1][d_bis] < min:
					min = couts[notes[n-k-1]][d][notes[n-k]][d_bis] + tc[k-1][d_bis]
					index = d_bis
			fingers[k][d] = index
			tc[k][d] = min
	return [tc, fingers]


def minCost(couts, notes): 
	tc = dynamicTable(couts, notes)[0]
	cost = tc[len(notes)-1][indexOfMinValue(tc[len(notes)-1])]
	fingers = findFingers(dynamicTable(couts, notes)[1], indexOfMinValue(tc[len(notes)-1]), len(notes))
	return [fingers, cost]
    
def dynamique(couts, notes):
	start = time.time()
	cost = minCost(couts, notes)
	end = time.time()
	temps = end - start
	result = [cost[0], cost[1], round(temps*1000)]
	return result
    
    
def main(argv):
	file = open(argv[1], "r")
	n = file.readline()
	file.close()
	notes = readFile(argv[1])
	load_file = np.loadtxt('cout_transition.txt', dtype=int)
	cout_transition = load_file.reshape((24, 5, 24, 5))
	
	result = dynamique(cout_transition, notes)
	
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
