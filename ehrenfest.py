# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:50:18 2022

@author: nikol
"""

'''
Ehrenfest-Chain aus Privault, Kapitel 4
'''

import numpy as np

def step(N,i):
    if(i==0):       #Randbedingungen umgesetzt
        return 1
    if(i==N):
        return N-1
    else:
        a=np.random.rand()
        if((i/N)>=a):
            return i-1
        else: return i+1

def ehrenfestsim(N,i,itnum): #N: Gesamtkapazität, i: wie viele Kugeln sind zu beginn in der linken Urne
    L=[i]
    current=i
    for j in range(itnum):
        newval=step(N,current)
        L.append(newval)
        current=newval
    return L
        
print(ehrenfestsim(10,1,10))
    
    