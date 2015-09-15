# -*- coding: cp1252 -*-
from Forme import *

class InputOutput:
    
    def __init__(self):pass
    
    def comparer(self,f1,f2):
        if f1.taille<f2.taille:
            return -1
        elif f1.taille>f2.taille:
            return 1
        else:
            return 0

    #fonction lecture des formes
    def lire_formes(self,nom_f):
        formes = []
        try:
            mon_fichier = open(nom_f, "r")
        except:
            print "Fichier introuvable !!"
            return
        global nb_ligne,nb_colonne
        liste = []
        nb_ligne = int(mon_fichier.readline())
        nb_colonne = int(mon_fichier.readline())
        lignes = mon_fichier.read().splitlines()
        lignes.remove("fin")
        lignes.pop(0)
        for ligne in lignes:
            if(ligne == "####"):
                formes.append(Forme(liste))
                del(liste[:])
            else:
                liste.append(ligne)
        #formes.sort(cmp=self.comparer,reverse=True)
        mon_fichier.close()
        return formes,nb_ligne,nb_colonne

    #fonction ecriture des formes
    def ecrire_formes(self,nom_f,resultats):
        mon_fichier = open(nom_f, "w")
        mon_fichier.write("il existe "+str(len(resultats))+" solutions\n")
        i = 0
        for mat in resultats:
            mon_fichier.write("solution numero  "+str(i)+"\n")
            for ligne in mat:
                s = ""
                for col in ligne:
                    s += col + " "
                mon_fichier.write(s[0:len(s)-1]+"\n")
            i += 1
        mon_fichier.close()
