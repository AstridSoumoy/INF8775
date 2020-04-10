import sys
import csv
import numpy as np
import time
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

def findBetterSolution(graph, PersonnesInfectes, k, resultat, noeudsInfectes, showWhat):
    newList = noeudsInfectes.copy()
    for node in newList:
        newGraph = graph.copy()
        newInfectes = PersonnesInfectes.copy()
        creerLien(newGraph, node[0], node[1])
        resultatTest = findSolution(newGraph, newInfectes, k)
        if(resultatTest <= 50):
            newList.remove(node)
            showRelations(newList, showWhat)

def showRelations(NodeList, showWhat):
    print("")  
    if showWhat == "relations":
        for node in NodeList:
            print(str(node[0]) + " " + str(node[1]))
    if showWhat == "number":
        print(str(len(NodeList)))  

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


    k = int(argv[1])
    showWhat = "number"
    
    if len(argv) == 3:
        if argv[2] == "-p":
            showWhat = "relations"
    # On get les noeuds qui pose problemes
    noeudsInfectes = []
    for i in range(0, len(graph)):
        noeuds = getNoeudsInfectees(graph, i, k, PersonnesInfectes)
        noeudsInfectes += noeuds

    listNoeudSupression = selectionMauvaisNoeuds(noeudsInfectes)

    graphTemp = graph
    #Initialisation du premier passage
    MeilleurListeNoeudsSuprrimer = []
    for index in range(0, len(noeudsInfectes)):
        couperLien(graphTemp, noeudsInfectes[index][0], noeudsInfectes[index][1])
    resultat = findSolution(graphTemp, PersonnesInfectes, k)
    if(resultat < 50):
        MeilleurListeNoeudsSuprrimer = noeudsInfectes

    showRelations(MeilleurListeNoeudsSuprrimer, showWhat)

    findBetterSolution(graph, PersonnesInfectes, k, resultat, noeudsInfectes, showWhat)




    return

if __name__ == "__main__":
    main(sys.argv[1:])
