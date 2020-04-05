import sys
import csv
import numpy
import time


def readFile(arg): 
    file = open(arg, "r")
    file.readline()
    A = []
    for line in file:
        line = line.strip()
        line = line.replace("\t", ",")
        if len(line) > 0:
            A.append(map(int, line.split(',')))
    file.close()

    return A


def printMatrix(A, B):
	matrix = conventional_multiply(A,B)
	for line in matrix:
		print("\t".join(map(str,line)))
	return

def printTime(A, B):
    start_time = time.time()
    matrix = conventional_multiply(A,B)
    print(round((time.time() - start_time)*1000, 5))
    return
        

def conventional_multiply(A, B):
    n = len(A)
    result = [[0 for i in xrange(n)] for j in xrange(n)]	
    for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				result[i][j] += A[i][k] * B[k][j]
    return result

def main(argv):

	file = open(argv[1], "r")
	n = file.readline()
	file.close()
	A = readFile(argv[1])
	B =  readFile(argv[2])
	for arg in argv:
		if arg == "-t":
			printTime(A,B)
		if arg == "-p":
			printMatrix(A,B)
	if len(argv) == 3:
		printMatrix(A,B)
		printTime(A,B)
	return
  
if __name__ == "__main__":
    main(sys.argv[1:])


    
