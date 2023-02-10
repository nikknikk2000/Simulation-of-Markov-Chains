Repositoryinhalt:

1) ehrenfest1.py: Es wird das Ehrenfestmodell modelliert. Bei diesem gibt es zwei 
                  miteinander verbundene Kammern, in denen sich zu Beginn insgesamt N Kugeln 
                  befinden. Zu jedem Zeipunkt wechselt genau ein Teilchen entweder von der linken
                  in die rechte oder (exklusives oder) von der rechten in die linke Kammer.
                  Die Zustände sind also die Anzahl der Kugeln (0,1,...,N), die sich in der linken
                  Kammer befinden. Es wird davon ausgegangen, dass die Übergangswahrscheinlich-
                  keiten wie folgt gegeben sind.X_n gibt an, wie viele Kugeln sich zum Zeitpunkt
                  n in der linken Kammer befinden.
                      {P(X_(n+1)=1|X_n=0)=1
                      P(X_(n+1)=N-1|X_n=N)=1
                      P(X_(n+1)=X_n-1|X_n=n)=i/N
                      P(X_(n+1)=X_n+1|X_n=n)=(N-i)/N}  
                  
                  
                  Es wird untersucht, wie
                  
                  Es wird untersucht, wie viele Kugeln sich zum jeweiligen Zeitpunkt in der linken
                  Kammer befinden.
                  Das Programm simuliert die Markovkette und stellt anschließend graphisch dar, 
                  wie viele Kugeln sich zum Zeitpunkt n in der linken Kammer befinden.
                  Das Programm wird mit N=10, i=5 aufgerufen und es werden 75 Schritte simuliert.
   
2) markovmusic.rb: die Markovkette (X_n) aus Beispiel 3.5 wird in Sonic Pi implementiert. Es gilt X_0=3 Jedem Zustand wird ein Ton zugeordnet, die erzeugte Tonfolge wird   zusammen mit einer Hintergrundmusik in Dauerschleife abgespielt.
   
3) markovcouplingmusicrb: es werden zwei unabhängige Markovketten (X_n) und (Y_n) in Sonic Pi bis zum Couplingzeitpunkt simuliert. (X_n) und (Y_n) besitzen als              Übergangsmatrix beide die Übergangsmatrix aus Beispiel 3.5 . Es gilt X_0=1 und Y_0=4. Es wird wiederum jedem Zustand ein Ton zugeordnet. Die Realisierungen von (X_n)      und (Y_n) werden 
   gleichzeitig abgespielt.
  
4) markovmusiccoupling_example1.wav: Beispielaudio, dass mit dem Programm markovcouplingmusicrb generiert wurde.

5) markovmusicexample1.wav: Beispielaudio, dass mit dem Programm markovmusic.rb generiert wurde.
   
6) chessrw1.py: Es werden ein weißer und ein schwarzer Springer simuliert, die auf den Feldern A8 bzw. H1 stehen. Weiß ist zuerst am Zug. Die Springer ziehen gemäß den 
   gängigen Schachregeln. Das Spiel endet, wenn ein Springer den anderen geschlagen hat. 
   
   Wie werden die Züge bestimmt?
   1)Die zulässigen Züge werden ermittelt
   2)Einer der Züge wird "gleichverteilt" ausgewählt
   
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

   Das Programm chessrw1.py simuliert das beschriebene Spiel und erstellt eine Animation,
   die unter dem Dateinamen chessSim.gif gespeichert wird.
