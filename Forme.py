# -*- coding: cp1252 -*-
def creer_matrice(longeur, largeur):
    liste = [["0"]*largeur for i in range(longeur)]
    return liste

class Forme: 
    def __init__(self,liste): 
        self.n = len(liste)
        self.m = len(liste[0])
        self.taille = 0
        self.mat = creer_matrice(self.n,self.m)
        i = 0
        for l in liste:
            j = 0
            while j < len(l):
                self.mat[i][j] = l[j]
                if l[j] != '0':
                    self.taille += 1
                j += 1
            i += 1
        self.smats = []
