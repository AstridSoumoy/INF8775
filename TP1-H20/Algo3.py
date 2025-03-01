import sys
import csv
import numpy
from optparse import OptionParser
from math import ceil, log
import time
from Algo1 import readFile


def printMatrix(A, B):
	matrix = strassenR(A,B)
	for line in matrix:
		print("\t".join(map(str,line)))
	return

def printTime(A, B):
    start_time = time.time()
    matrix = strassenR(A,B)
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

def add(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassenR(A, B):
    n = len(A)
    seuil = 4
    if n <= seuil:
	    return conventional_multiply(A, B)
    else:
        # initializing the new sub-matrices
		newSize = n/2
		a11 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		a12 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		a21 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		a22 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

		b11 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		b12 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		b21 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		b22 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

		aResult = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
		bResult = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        # dividing the matrices in 4 sub-matrices:
		for i in xrange(0, newSize):
			for j in xrange(0, newSize):
				a11[i][j] = A[i][j]            # top left
				a12[i][j] = A[i][j + newSize]    # top right
				a21[i][j] = A[i + newSize][j]    # bottom left
				a22[i][j] = A[i + newSize][j + newSize] # bottom right

				b11[i][j] = B[i][j]            # top left
				b12[i][j] = B[i][j + newSize]    # top right
				b21[i][j] = B[i + newSize][j]    # bottom left
				b22[i][j] = B[i + newSize][j + newSize] # bottom right

        # Calculating p1 to p7:
		aResult = add(a11, a22)
		bResult = add(b11, b22)
 		p1 = strassenR(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

		aResult = add(a21, a22)      # a21 + a22
		p2 = strassenR(aResult, b11)  # p2 = (a21+a22) * (b11)

		bResult = subtract(b12, b22) # b12 - b22
		p3 = strassenR(a11, bResult)  # p3 = (a11) * (b12 - b22)

		bResult = subtract(b21, b11) # b21 - b11
		p4 =strassenR(a22, bResult)   # p4 = (a22) * (b21 - b11)

		aResult = add(a11, a12)      # a11 + a12
		p5 = strassenR(aResult, b22)  # p5 = (a11+a12) * (b22)   

		aResult = subtract(a21, a11) # a21 - a11
		bResult = add(b11, b12)      # b11 + b12
		p6 = strassenR(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

		aResult = subtract(a12, a22) # a12 - a22
		bResult = add(b21, b22)      # b21 + b22
		p7 = strassenR(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
		c12 = add(p3, p5) # c12 = p3 + p5
		c21 = add(p2, p4)  # c21 = p2 + p4

		aResult = add(p1, p4) # p1 + p4
		bResult = add(aResult, p7) # p1 + p4 + p7
		c11 = subtract(bResult, p5) # c11 = p1 + p4 - p5 + p7

		aResult = add(p1, p3) # p1 + p3
		bResult = add(aResult, p6) # p1 + p3 + p6
		c22 = subtract(bResult, p2) # c22 = p1 + p3 - p2 + p6

		C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
		for i in xrange(0, newSize):
			for j in xrange(0, newSize):
				C[i][j] = c11[i][j]
				C[i][j + newSize] = c12[i][j]
				C[i + newSize][j] = c21[i][j]
				C[i + newSize][j + newSize] = c22[i][j]
		return C


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


    
