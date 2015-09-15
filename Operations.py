# -*- coding: cp1252 -*-
import copy

class Operations:
    
    def __init__(self):
        self.nb = 0
    
    def creer_matrice(self,longeur, largeur):
        liste = [["0"]*largeur for i in range(longeur)]
        return liste
    
    def insertMat(self,forme,i,j,mat_res):
        temp = j
        for k in range(0,forme.n):
            for l in range(0,forme.m):
                if forme.mat[k][l] != "0":
                    mat_res[i][j] = forme.mat[k][l]
                j += 1
            j = temp
            i += 1
        return mat_res

    def testValidite(self,forme,i,j,mat_res):
        test = True
        k = i
        while k < i + forme.n and test:
            l = j
            while l < j + forme.m and test:
                if mat_res[k][l] != '0' and forme.mat[k-i][l-j] != '0':
                    test = False
                l += 1
            k += 1
        return test

    def recherche(self,indice,mat,formes,nb_ligne,nb_colonne,resultats):
        for i in range(0,nb_ligne - formes[indice].n + 1):
            for j in range(0,nb_colonne - formes[indice].m + 1):
                if(self.testValidite(formes[indice],i,j,mat)):
                    tempMat = self.insertMat(formes[indice],i,j,copy.deepcopy(mat))
                    if(indice == len(formes) - 1):
                        resultats.append(tempMat)
                        #print(len(resultats)," Solutions trouvees.")
                    else:
                        self.recherche(copy.deepcopy(indice + 1), tempMat,formes,nb_ligne,nb_colonne,resultats)           
        return resultats
    
    def rechercheUNE(self,indice,mat,formes,nb_ligne,nb_colonne,resultats):
        if(len(resultats) == 0):
            for i in range(0,nb_ligne - formes[indice].n + 1):
                for j in range(0,nb_colonne - formes[indice].m + 1):
                    if(self.testValidite(formes[indice],i,j,mat)):
                        tempMat = self.insertMat(formes[indice],i,j,copy.deepcopy(mat))
                        if(indice == len(formes) - 1):
                            resultats.append(tempMat)
                            print("Une Solution est trouveé.")
                        else:
                            self.rechercheUNE(copy.deepcopy(indice + 1), tempMat,formes,nb_ligne,nb_colonne,resultats)           
        return resultats
    
    def combienRotation(self, matrice,n,m):
        plein=True
        for i in range(0,n):
            for j in range(0,m):
                if matrice[i][j]=="0":
                    plein=False
        return plein

    def rotationDroit(self,forme):
        w=forme.n
        l=forme.m
        matTemp=self.creer_matrice(l,w)
        for i in range(0,l):
            for j in range(0,w):
                matTemp[i][j] = forme.mat[w - j - 1][i]
        forme.n=l
        forme.m=w
        forme.mat=matTemp
        return forme
    
    def getRotationsPossible(self,formes,nb_ligne,nb_colonne):
        for i in range(0,len(formes)):
            plein=self.combienRotation(formes[i].mat,formes[i].n,formes[i].m)
            formes[i].smats.append(formes[i])
            if plein and not(formes[i].n==formes[i].m):
                if plein and not(formes[i].n==formes[i].m):
                    formes[i].smats.append(self.rotationDroit(copy.deepcopy(formes[i])))
            if not plein:
                if formes[i].m <= nb_ligne and formes[i].n <= nb_colonne:
                    rd = self.rotationDroit(copy.deepcopy(formes[i]))
                    rdd = self.rotationDroit(copy.deepcopy(formes[i].smats[len(formes[i].smats)-1]))
                    rg = self.rotationDroit(copy.deepcopy(formes[i].smats[len(formes[i].smats)-1]))
                    if rd.mat != rdd.mat:
                        if rd.mat != rg.mat:
                            formes[i].smats.append(rd)
                            formes[i].smats.append(rdd)
                            formes[i].smats.append(rg)
                        else:
                            formes[i].smats.append(rd)
                else:
                    formes[i].smats.append(self.rotationDroit(copy.deepcopy(self.rotationDroit(copy.deepcopy(formes[i])))))
        return formes
    
    def rechercheRotation(self,indice,mat,formes,nb_ligne,nb_colonne,resultats):
        for k in range(0,len(formes[indice].smats)):
            for i in range(0,nb_ligne - formes[indice].smats[k].n + 1):
                for j in range(0,nb_colonne - formes[indice].smats[k].m + 1):
                    if(self.testValidite(formes[indice].smats[k],i,j,mat)):
                        tempMat = self.insertMat(formes[indice].smats[k],i,j,copy.deepcopy(mat))
                        if(indice == len(formes) - 1):
                            resultats.append(tempMat)
                            #print(len(resultats)," Solutions trouvees.")
                        else:
                            self.rechercheRotation(copy.deepcopy(indice + 1), tempMat,formes,nb_ligne,nb_colonne,resultats)           
        return resultats
