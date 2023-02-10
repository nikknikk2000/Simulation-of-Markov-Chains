# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:06:28 2023

@author: nikol
"""



import matplotlib.pyplot as plt
import numpy as np

#Methode firststep wird nicht benötigt, da vorgegeben ist, wie viele Kugeln zu Beginn in der rechten/linken Kammer sind

#step: bewegt gemäß den Übergangswahrscheinlichkeiten eine Kugel von der linken in die rechte Kammer oder von der rechten in die linke Kammer 
def step(N,i):  #N: Gesamtanzahl der Kugeln, i: Anzahl der Kugeln auf linker Seite
    if(i==0):       #wenn auf Linker Seite 0 Kugeln sind kommt mit Wkt. 1 eine Kugel von der rechten auf die linke Seite
        return 1    
    if(i==N):
        return N-1  #wenn auf Linker Seite N Kugeln sind kommt mit Wkt. 1 eine Kugel von der linken auf die rechte Seite
   
    else:
        a=np.random.rand()
        if((i/N)>=a):
            return i-1
        else: 
         return i+1
        

                   
def simulate(N,i,itnum):#N: Gesamtanzahl der Kugeln, i: Anzahl Kugeln in linker Kammer zu Beginn, itnum: Anzahl der Iterationsschritte
    L=[]  #Liste um zu speichern, wie viele Kugeln zu Zeitpunkt n auf linker Seite sind
    currenti=i
    L.append(currenti)
    for i in range(itnum):
         currenti=step(N,currenti) 
         L.append(currenti)
    return L 


S=simulate(10,5,75)

'''Plot erstellen'''

lin=np.linspace(0,75,76).T
plt.plot(lin,S,linestyle='dashed',marker='s')
plt.xlabel('n')
plt.ylabel('Kugeln in der Linken Kammer')
plt.show()


