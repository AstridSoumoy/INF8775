import sys
import csv
import numpy as np
import time
import pandas as pd
import sys
from random import *

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
    verificationEntourage(graph, listInfectee, k)
    return int((100* len(listInfectee))/len(graph))



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
        #print(listInfectee)
        if (not (i in listInfectee)) & estInfectee(graph[i], listInfectee, k, graph):
            listInfectee.append(i)
            verificationEntourage(graph, listInfectee, k)


def getNoeudsInfectees(graph, index, k, listInfectee):
    count = 0
    #print(count)
    noeudSupprimer = []
    for i in range(0, len(graph[index])):
        valeur = graph[index][i]
        #print(valeur)
        if ((valeur == 1) & (i in listInfectee)):
            #print("on est dans le premier if")
            if(count == k-1):
                #print("on est dans le deuxieme if")
                noeud = (index, i) #str(index) + " " + str(i)
                noeudSupprimer.append(noeud)
            else:
                #print("on est dans le else")
                count += 1
    #print(count)
    return noeudSupprimer


def couperLien(graph, index1, index2):
    graph[index1][index2] = 0
    graph[index2][index1] = 0

def creerLien(graph, index1, index2):
    graph[index1][index2] = 1
    graph[index2][index1] = 1

def selectionMauvaisNoeuds(noeudsInfectee):
    listSupression = []
    nombreDeSupression = randint(0, len(noeudsInfectee) - 1)
    while(len(listSupression) < nombreDeSupression):
        suppressionAleatoire = randint(0, len(noeudsInfectee) -1)
        #print("supression: ")
        #print(suppressionAleatoire)
        if not(suppressionAleatoire in listSupression):
            #print("AJOUT")
            listSupression.append(suppressionAleatoire)

    return listSupression



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
    #print(PermiereLigne)


    k = 2  # argv[1]
    #if argv[2] == "-p":
    #    print("-p entered")


    # On get les noeuds qui pose problemes
    noeudsInfectee = []
    for i in range(0, len(graph)):
        noeuds = getNoeudsInfectees(graph, i, k, PersonnesInfectes)
        noeudsInfectee += noeuds
    #for i in range(0, len(noeudsInfectee)):
    #    print(noeudsInfectee[i])
    #print(graph)

    listNoeudSupression = selectionMauvaisNoeuds(noeudsInfectee)


#Initialisation du premier passage 
    MeilleurListeNoeudsSuprrimer = []
    for index in range(0, len(noeudsInfectee)):
        couperLien(graph, noeudsInfectee[index][0], noeudsInfectee[index][1])
    #print(graph)
    resultat = findSolution(graph, PersonnesInfectes, k)
    if(resultat < 50):
        MeilleurListeNoeudsSuprrimer = noeudsInfectee

    print(MeilleurListeNoeudsSuprrimer)
    print(resultat)
    testindex = 6

    creerLien(graph, MeilleurListeNoeudsSuprrimer[testindex][0], MeilleurListeNoeudsSuprrimer[testindex][1])
    resultat = findSolution(graph, PersonnesInfectes, k)
    if(resultat < 50):
        MeilleurListeNoeudsSuprrimer.pop(testindex)
    print(MeilleurListeNoeudsSuprrimer)
    print(resultat)
    return

if __name__ == "__main__":
    main(sys.argv[1:])
