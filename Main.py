# -*- coding: cp1252 -*-
import time
from Forme import *
from InputOutput import *
from Operations import *

if __name__ == '__main__': 
    
    formes = []
    rotFormes=[]
    resultats = []
    resultatsRotation = []
    nb_ligne = 0
    nb_colonne = 0
    o = Operations()
    io = InputOutput()
    
    print("*** Solutionneur Casse-tête ***")
    
    f_in = raw_input("Entrez nom de fichier d'entrée : ")
    while f_in == "":
        print "Erreur : champ vide !!"
        f_in = raw_input("Entrez nom de fichier d'entrée : ")
    
    formes,nb_ligne,nb_colonne = io.lire_formes(f_in)
    
    while 1:
        resultats = []
        resultatsRotation = []
        
        print "\n Que désirez-vous ? : \n\
        1 - Trouver une solution.\n\
        2 - Trouver tous les solutions.\n\
        3 - Trouver tous les solutions avec rotation des formes.\n\
        0 - Quitter.\n "
        choix=raw_input("Votre choix ? : ")
     
        if choix=="1":
            print "*** Une solution ***"
            tps1 = time.clock()
            bigMat = creer_matrice(nb_ligne,nb_colonne)
            resultats = o.rechercheUNE(0,bigMat,formes,nb_ligne,nb_colonne,resultats)
            io.ecrire_formes("sortiUNE.txt",resultats)
            tps2 = time.clock()
            print("Temps d'exécution : ",tps2 - tps1, " s")
        elif choix=="2":
            print "*** Tous les solutions ***"
            tps1 = time.clock()
            bigMat = creer_matrice(nb_ligne,nb_colonne)
            resultats=o.recherche(0,bigMat,formes,nb_ligne,nb_colonne,resultats)
            io.ecrire_formes("sortiTousS.txt",resultats)
            tps2 = time.clock()
            print("Temps d'exécution : ",tps2 - tps1, " s")
        elif choix=="3":
            print "*** Tous les solutions avec rotations des formes ***"
            tps1 = time.clock()
            formes = o.getRotationsPossible(copy.deepcopy(formes),nb_ligne,nb_colonne)
            bigMat = creer_matrice(nb_ligne,nb_colonne)
            resultatsRotation = o.rechercheRotation(0,bigMat,formes,nb_ligne,nb_colonne,resultats)
            io.ecrire_formes("sortiTouSRotation.txt",resultatsRotation)
            tps2 = time.clock()
            print("Temps d'exécution : ",tps2 - tps1, " s")
        elif choix=="0":
            print "Au revoir !"
            break
     
        else:
            print "[0..3] uniquement s.v.p !!"
            