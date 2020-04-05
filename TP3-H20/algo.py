import sys
import csv
import numpy as np
import time
import pandas as pd 


def readFile(arg): 
    file = open(arg, "r")
    A = []
    count = 0
    for line in file:
        count += 1
        line = line.strip()
        line = line.replace("\t", ",")
        if len(line) > 0:
            A.append(map(int, line.split(' ')))
    file.close()
    premiereLigne = A[0]
    derniereLigne = A[count - 1]
    A.remove(A[0])
    A.remove(A[count - 2])
    return premiereLigne, derniereLigne, A


def main(argv):
    file = open(argv[0], "r")
    lines = file.readlines()
    countLines = len(lines)
    file.close()


    #premieiereLigne = np.loadtxt(lines[0])
    #derniereLigne = np.loadtxt(lines[countLines])

    #f = open("yourfile.txt","w")
    #for i in range(1,countLines-1):
    #    f.write(lines[i])
    #graphe = np.loadtxt(f)
    #f.close()


    notes = readFile(argv[0])
    PermiereLigne = list(notes[0])
    DerniereLigne = list(notes[1])
    A = list(notes[2])
    graph = np.array([np.array(list(mapGraph)) for mapGraph in A])
    print(PermiereLigne)
    print(DerniereLigne)
    print(graph)
    return

if __name__ == "__main__":
    main(sys.argv[1:])
