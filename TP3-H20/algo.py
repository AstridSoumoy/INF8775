import sys
import csv
import numpy as np
import time
import pandas as pd
import sys


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

def findSolution(graph, listInfectee, k):
    print(getPourcentagePersonneInfectee(graph, listInfectee, k))

def getPourcentagePersonneInfectee(graph, listInfectee, k):
    verificationEntourage(graph, listInfectee, k)
    return (100* len(listInfectee))/len(graph)



def estInfectee(ligne, listInfectee, k, graph):
    count = 0
    for i in range(0, len(graph)):
        if (i in listInfectee) and (ligne[i] == 1):
            count += 1
    if count >= k:
        return True
    else:
        return False


def verificationEntourage(graph, listInfectee, k):
    for i in range(0, len(graph)):
        print(listInfectee)
        if (not (i in listInfectee)) & estInfectee(graph[i], listInfectee, k, graph):
            listInfectee.append(i)
            verificationEntourage(graph, listInfectee, k)





def main(argv):
    #sys.setrecursionlimit(10**6)
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
    tailleDeLaPopulation = PermiereLigne[0]
    nombrePersonnesMalades = PermiereLigne[1]
    PersonnesInfectes = list(notes[1])
    A = list(notes[2])
    graph = np.array([np.array(list(mapGraph)) for mapGraph in A])
    print(PermiereLigne)
    print(PersonnesInfectes)
    print(graph)
    k = argv[1]
    if argv[2] == "-p":
        print("-p entered")
    findSolution(graph, PersonnesInfectes, k)
    return

if __name__ == "__main__":
    main(sys.argv[1:])
