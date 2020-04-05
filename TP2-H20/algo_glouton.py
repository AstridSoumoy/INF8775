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

def findNext(previousFinger, previousNoteIndex, couts, notes):
	cout = couts[notes[previousNoteIndex]][previousFinger][notes[previousNoteIndex + 1]][0]
	result = [0, cout]
	for i in range(0,5):
		if  cout > couts[notes[previousNoteIndex]][previousFinger][notes[previousNoteIndex + 1]][i]:
			cout = couts[notes[previousNoteIndex]][previousFinger][notes[previousNoteIndex + 1]][i]
			result = [i, cout]
	return result
	
	
def findFirst(couts, notes):
	cout = couts[notes[0]][0][notes[1]][0]
	result = [0, 0, cout]
	for i in range(0,5):
		for j in range(0,5):
			if  cout > couts[notes[0]][i][notes[1]][j]:
				cout = couts[notes[0]][i][notes[1]][j]
				result = [i, j, cout]
	return result
    
def glouton(couts, notes):
	fingers = []
	start = time.time()
	fingers.append(findFirst(couts, notes)[0])
	fingers.append(findFirst(couts, notes)[1])
	cout = findFirst(couts, notes)[2]
	for i in range(1,len(notes) - 1):
		cout += findNext(fingers[len(fingers) - 1], i, couts, notes)[1]
		fingers.append(findNext(fingers[len(fingers) - 1], i, couts, notes)[0])
	end = time.time()
	temps = end - start
	result = [fingers, cout, round(temps*1000)]
	return result
	
    
def main(argv):
	file = open(argv[1], "r")
	n = file.readline()
	file.close()
	notes = readFile(argv[1])
	load_file = np.loadtxt('cout_transition.txt', dtype=int)
	cout_transition = load_file.reshape((24, 5, 24, 5))
	
	result = glouton(cout_transition, notes)
	
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
