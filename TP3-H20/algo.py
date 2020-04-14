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
        if (not (i in listInfectee)) & estInfectee(graph[i], listInfectee, k, graph):
            listInfectee.append(i)
            verificationEntourage(graph, listInfectee, k)


def getNoeudsInfectees(graph, index, k, listInfectee):
    count = 0
    noeudSupprimer = []
    for i in range(0, len(graph[index])):
        valeur = graph[index][i]
        if ((valeur == 1) & (i in listInfectee)):
            if(count == k-1):
                noeud = (index, i)
                noeudSupprimer.append(noeud)
            else:
                count += 1
    return noeudSupprimer

def getNoeudsInfectees2(graph, index, k, listInfectee):
    count = 0
    noeudSupprimer = []
    tempListInfectee = listInfectee.copy()
    while(len(tempListInfectee) != 0):
        noeudAleatoire = randint(0, len(tempListInfectee) - 1)
        valeur = graph[index][tempListInfectee[noeudAleatoire]]
        if (valeur == 1):
            if(count == k-1):
                noeud = (index, tempListInfectee[noeudAleatoire])
                noeudSupprimer.append(noeud)
            else:
                count += 1
            tempListInfectee.remove(tempListInfectee[noeudAleatoire])
        else:
            tempListInfectee.remove(tempListInfectee[noeudAleatoire])
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
        if not(suppressionAleatoire in listSupression):
            listSupression.append(suppressionAleatoire)

    return listSupression

def findBetterSolution(graph, PersonnesInfectes, k, noeudsInfectes, showWhat, betterSolution):
    newList = noeudsInfectes.copy()
    for node in newList:
        newGraph = graph.copy()
        newInfectes = PersonnesInfectes.copy()
        creerLien(newGraph, node[0], node[1])
        resultatTest = findSolution(newGraph, newInfectes, k)
        if resultatTest <= 50:
            newList.remove(node)
            if len(newList) < len(betterSolution):
                showRelations(newList, showWhat)
    return newList


def showRelations(NodeList, showWhat):
    print("")  
    if showWhat == "relations":
        for node in NodeList:
            print(str(node[0]) + " " + str(node[1]))
    if showWhat == "number":
        print(str(len(NodeList))) 
    sys.stdout.flush()

def initFirstSolution(graph,PersonnesInfectes, k, noeudsInfectes, showWhat): 
    graphTemp = graph
    MeilleurListeNoeudsSuprrimer = []
    for index in range(0, len(noeudsInfectes)):
        couperLien(graphTemp, noeudsInfectes[index][0], noeudsInfectes[index][1])
    resultat = findSolution(graphTemp, PersonnesInfectes, k)
    if(resultat < 50):
        MeilleurListeNoeudsSuprrimer = noeudsInfectes
        showRelations(MeilleurListeNoeudsSuprrimer, showWhat)
    return MeilleurListeNoeudsSuprrimer

def getNoeudsInfectes(graph, k, PersonnesInfectes):
    noeudsInfectes = []
    for i in range(0, len(graph)):
        noeuds = getNoeudsInfectees(graph, i, k, PersonnesInfectes)
        noeudsInfectes += noeuds
    return noeudsInfectes



def findBetterSolutionRandomly(graph, PersonnesInfectes, k, noeudsInfectes, showWhat, betterSolution):
    newList = noeudsInfectes.copy()
    while True:
        for node in newList:
            newGraph = graph.copy()
            newInfectes = PersonnesInfectes.copy()
            creerLien(newGraph, node[0], node[1])
            resultatTest = findSolution(newGraph, newInfectes, k)
            if(resultatTest <= 50):
                    newList.remove(node)
                    if len(newList) < len(betterSolution):
                        showRelations(newList, showWhat)
            for node2 in newList:
                creerLien(newGraph, node2[0], node2[1])
                resultatTest = findSolution(newGraph, newInfectes, k)
                if(resultatTest <= 50):
                    newList.remove(node)
                    newList.remove(node2)
                    if len(newList) < len(betterSolution):
                        showRelations(newList, showWhat)
                for node3 in newList:
                    creerLien(newGraph, node3[0], node3[1])
                    resultatTest = findSolution(newGraph, newInfectes, k)
                    if(resultatTest <= 50):
                        newList.remove(node)
                        newList.remove(node2)
                        newList.remove(node3)
                        if len(newList) < len(betterSolution):
                            showRelations(newList, showWhat)
    return newList

def findBetterSolutionRandomly2(graph, PersonnesInfectes, k, noeudsInfectes, showWhat, betterSolution):
    newList = []
    while True:
        newGraph = graph.copy()
        newInfectes = PersonnesInfectes.copy()
        listSuppression = selectionMauvaisNoeuds(noeudsInfectes)
        for i in range(0, len(listSuppression)):
            noeud = noeudsInfectes[listSuppression[i]]
            couperLien(newGraph, noeud[0], noeud[1])
            newList += noeud
            resultatTest = findSolution(newGraph, newInfectes, k)
        if len(newList) < len(betterSolution):
            showRelations(newList, showWhat)
    return newList

def getEchantillonAleatoire(graph, k, PersonnesInfectes):
    #ECHANTILLON ALEATOIRE !!!!
    mauvaixNoeuds = []
    for i in range(0, len(graph)):
        noeud = getNoeudsInfectees2(graph, i, k, PersonnesInfectes)
        mauvaixNoeuds += noeud

    
    #for noeud in mauvaixNoeuds:
        #print(noeud)

    return mauvaixNoeuds


def main(argv):
    file = open(argv[0], "r")
    lines = file.readlines()
    countLines = len(lines)
    file.close()


    notes = readFile(argv[0])
    PermiereLigne = list(notes[0])
    tailleDeLaPopulation = PermiereLigne[0]
    nombrePersonnesMalades = PermiereLigne[1]
    PersonnesInfectes = list(notes[1])
    A = list(notes[2])
    graph = np.array([np.array(list(mapGraph)) for mapGraph in A])


    k = int(argv[1])
    showWhat = "number"
    
    if len(argv) == 3:
        if argv[2] == "-p":
            showWhat = "relations"



    #test = getEchantillonAleatoire(graph, k, PersonnesInfectes)
    # On get les noeuds qui pose problemes
    noeudsInfectes = getNoeudsInfectes(graph, k, PersonnesInfectes)
    
    betterSolution = initFirstSolution(graph,PersonnesInfectes, k, noeudsInfectes, showWhat)
    #betterSolution = findBetterSolution(graph, PersonnesInfectes, k, test, showWhat, betterSolution)
    #betterSolution = findBetterSolutionRandomly2(graph, PersonnesInfectes, k, noeudsInfectes, showWhat, betterSolution)

    return

if __name__ == "__main__":
    main(sys.argv[1:])
