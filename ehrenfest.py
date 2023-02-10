# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:06:28 2023

@author: nikol
"""


'''
Im Folgenden wird das Ehrenfestmodell modelliert. Bei diesem gibt es zwei 
miteinander verbundene Kammern, in denen sich zu Beginn insgesamt N Kugeln 
befinden. Zu jedem Zeipunkt wechselt genau ein Teilchen entweder von der linken
in die rechte oder (exklusives oder) von der rechten in die linke Kammer.
Die Zustände sind also die Anzahl der Kugeln (0,1,...,N), die sich in der linken
Kammer befinden. Es wird davon ausgegangen, dass die Übergangswahrscheinlich-
keiten wie folgt gegeben sind.X_n gibt an, wie viele Kugeln sich zum Zeitpunkt
n in der linken Kammer befinden.
    P(X_(n+1)=1|X_n=0)=1
    P(X_(n+1)=N-1|X_n=N)=1
    P(X_(n+1)=X_n-1|X_n=n)=i/N
    P(X_(n+1)=X_n+1|X_n=n)=(N-i)/N
Quelle: [14]    

Es wird untersucht, wie viele Kugeln sich zum jeweiligen Zeitpunkt in der linken
Kammer befinden.

Das Programm simuliert die Markovkette und stellt anschließend graphisch dar, 
wie viele Kugeln sich zum Zeitpunkt n in der linken Kammer befinden.
Das Programm wird hier mit N=10, i=5 aufgerufen und es werden 75 Schritte simuliert.
'''
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


