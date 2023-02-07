# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:29:19 2022

@author: nikol
"""

'''knight vs bishop, completely random'''

import numpy as np
def stepk(current):
    pos=[]
    dir=[[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
    
    for el in dir:
        if(0<=el[0]+current[0]<=7 and 0<=el[1]+current[1]<=7 ):
            pos.append(el)
    a=(np.random.randint(0,len(pos)))
    return([current[0]+pos[a][0],current[1]+pos[a][1]])




def stepb(current): #ermittelt zufälliges feld
    pot=[]
   
    directions=[[-1,1],[1,1],[1,-1],[-1,-1]]
     # erste richtung
    direc=[-1,1]
    pos=[current[0]+direc[0],current[1]+direc[1]]
    while(pos[0]>=0 and pos[1]<=7):
        pot.append(pos)
        pos=[pos[0]+direc[0],pos[1]+direc[1]]

    #zweite richtung
    direc=[1,1]
    pos=[current[0]+direc[0],current[1]+direc[1]]
    while(pos[0]<=7 and pos[1]<=7):
        pot.append(pos)
        pos=[pos[0]+direc[0],pos[1]+direc[1]]

    #dritte richtung
    direc=[1,-1]
    pos=[current[0]+direc[0],current[1]+direc[1]]
    while(pos[0]<=7 and pos[1]>=0):
        pot.append(pos)
        pos=[pos[0]+direc[0],pos[1]+direc[1]]
    
    #vierte Richting
    direc=[-1,-1]
    pos=[current[0]+direc[0],current[1]+direc[1]]
    while(pos[0]>=0 and pos[1]>=0):
        pot.append(pos)
        pos=[pos[0]+direc[0],pos[1]+direc[1]]
    
    a=(np.random.randint(0,len(pot)))
    return pot[a]

def coupledrw(knight,bishop):
    moves=[]
    currentk=knight
    currentb=bishop
    i=1
    while(currentk!=currentb):
        if(i%2==0):
            currentk=stepk(currentk)
            moves.append(currentk)
        else:
            currentb=stepb(currentb)
            moves.append(currentb)
        i+=1
    return moves

#methode, die einzelnen feldnamen zurückgibt
def getfieldname(current):  #gibt den Namen des Feldes zurück, bekommt als argument liste, ich brauche startaufruf
    if(current[1]==0):
        return 'a'+str(8-current[0])
    elif(current[1]==1):
        return 'b'+str(8-current[0])
    elif(current[1]==2):
        return 'c'+str(8-current[0])
    elif(current[1]==3):
        return 'd'+str(8-current[0])
    elif(current[1]==4):
        return 'e'+str(8-current[0])
    elif(current[1]==5):
        return 'f'+str(8-current[0])
    elif(current[1]==6):
        return 'g'+str(8-current[0])
    elif(current[1]==7):
        return 'h'+str(8-current[0])
    



walk=coupledrw([0,0],[2,1])
for j in range(len(walk)):
    walk[j]=getfieldname(walk[j])
print(walk)







