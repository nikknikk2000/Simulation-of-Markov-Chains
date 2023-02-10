# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:45:22 2023

@author: nikol
"""

'''
Was wird simuliert? Ein weißer Springer steht auf einem Schachbrett auf dem Feld A8, ein schwarzer 
Springer steht auf dem Feld  H1. Weiß ist zuerst am Zug. Die Springer ziehen gemäß der
gängigen Schachregeln. Das Spiel endet, wenn ein Springer den anderen geschlagen hat.

Wie werden die Züge bestimmt? 
1) Die zulässigen Züge ermitteln
2) Einen dieser Züge "gleichverteilt" auswählen

Verbindung mit Markovketten: Man kann sich leicht überlegen, dass Schwarz immer gewinnt.
Da Schwarz als zweites zieht können der n-te Weiße und der n-te schwarze Zug zusammen betrachtet
werden.

Zustände: Die Felder des Schachbrettes werden abgezählt. Die Zustände haben die Gestalt
(x,y) mit x=1,...,64 und y=1,...,64.

Als Übergangswahrscheinlichkeiten wählt man das Produkt der Wahrscheinlichkeiten, dass 
der jeweilige Springer ausgehend von seiner aktuellen Position auf das jeweilige Feld zieht.

Als Startverteilung wählt man den Vektor, der an der Stelle 
("Zahl, die A8 zugeordnet ist"; "Zahl, die H1 zugeordnet ist").

Hierbei handelt es sich um ein Beispiel für independent coupling.

Das Folgende Programm Simuliert das beschriebene Spiel und erstellt eine Animation,
die unter dem Dateinamen chessSim.gif gespeichert wird.

 
'''



import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.colors import ListedColormap

#Methode ermittelt, auf welches Feld Springer zieht, der sich auf dem "Feld" current befindet
def stepk(current):
    pos=[]
    dir=[[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]] #Menge der "Richtungen", in die Springer ziehen könnte
    
   #es wird ermittelt, welche der Zugrichtungen zulässig ist
    for el in dir:  
        if(0<=el[0]+current[0]<=7 and 0<=el[1]+current[1]<=7 ):
            pos.append(el)
    a=(np.random.randint(0,len(pos))) #aus der Menge der zulässigen Richtungen wird eine Richtung ausgewählt, jede der Richtungen wird mit derselben Wkt. ausgewählt
    return ([current[0]+pos[a][0],current[1]+pos[a][1]])#neue Position des Springers wird ermittelt und zurückgegeben


def coupledrw(wknight,bknight): #erhält die (Start)-Position des weißen (wknight) und des schwarzen springers (bknight)
    moves=[] #Liste um Züge zu speichern
    currentwk=wknight #Anlegen von Variable, die aktuelle Position des weißen Springers angibt
    currentbk=bknight #Anlegen von Variable, die aktuelle Position des schwarzen Springers angibt
    i=0              #Hilsvariable, die verwendet wird um zu bestimmen, wer am Zug ist
    while(currentwk!=currentbk): #überprüft, ob die Springer auf demselben Feld stehen
        if(i%2==0):
            currentwk=stepk(currentwk) #weißer Springer zieht
            moves.append((1,currentwk))
        else:
            currentbk=stepk(currentbk) #schwarzer Springer zieht
            moves.append((0,currentbk)) 
        i+=1
    return moves #Liste mit Zügen wird zurückgegeben


def genam(wk,bk): #erhält position des weißen und des schwarzen springers

    cmap = ListedColormap(['g', 'y']) #Farbschema für Bretteinfärbung
    
    '''Beschriftung und Erstellung des Schachbrettes'''
    fig = plt.figure()
    plt.yticks(range(8), [8,7,6,5,4,3,2,1]) #y-Achse wird mit Buchstaben A bis H beschriftet
    plt.xticks(range(8),['A','B','C','D','E','F','G','H']) #x- Achse wird mit Zahlen von 1 bis 8 beschriftet

     
    axis = fig.add_subplot()
     
    board=np.array(([1,0]*4+[0,1]*4)*4).reshape((8,8))
    axis.matshow(board,cmap=cmap)
    
    '''Ziel: Figuren auf Brett platzieren'''
    setBlack=[ (u'\u265E',1,0)]        #erster Eintrag: unicode für schwarzen springer
    setWhite=[(u'\u2658',wk[0],wk[1])] #erster Eintrag: unicode für weißen Springer
    
    
    for i in setBlack:
          axis.text(i[1], i[2], i[0], va='center', ha='center') #plaziert schwarzen Springer auf Feld
            
          
    for i in setWhite:
          axis.text(i[1], i[2], i[0], va='center', ha='center', color='white') #plaziert weißen Springer auf Feld
         
     
    
    def runIt(k):
        axis.texts[k[0]].set_position((k[1],k[2])) #Zug wird ausgeführt
        return []
        
     
    def init(): #dummy-Methode, die für die Methode, die Animation erstellt benötigt wird...
        
        return []
    
    L=coupledrw(wk,bk)  #coupledrw wird aufgerufen, Liste mit Zügen wird erstellt

    setSequence=[(0,bk[0],bk[1]),(1,wk[0],wk[1])] #Züge werden in passendes Format gebracht
    for el in L:   #Zugfolge wird ausgeführt
        setSequence.append((el[0],el[1][0],el[1][1])) 

    
    
    anim = FuncAnimation(fig, runIt,        #es wird definiert was animiert wird
                        init_func = init,
                        frames = setSequence,
                        interval = 20,
                        blit = True)
    
    anim.save('chessSim.gif', writer = 'ffmpeg', fps = 0.5)  #erstellt Animation
    plt.close()

genam([7,7],[0,0]) #Methodenaufruf, weißer springer auf A8, schwarzer Springer auf H1