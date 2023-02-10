
P=[[0,6,0,0,0],[0,0,6,0,0],[0,0,0,6,0],[2,2,0,0,2],[3,0,0,0,3]] #Matrixeinträge wurden mit 6 multipliziert, da Programm nicht mit Brüchen arbeitet


define:step do |i|  #step macht einen Iterationsschritt, gibt zustand zurück,
  sum=0
  counter=0
  itnum=0
  #use_random_seed Time.now.to_i
  val=rand(6) #zufallszahl zwischen 0 und 6 erzeugen
  while sum<=val do
    sum=sum+P[i][itnum]
    itnum=itnum+1
    
    
  end
  return itnum-1 #wird einmal zu oft erhöht...
end



define:walk do |itnum|  #führt walk aus und gibt liste mit zuständen zurück
  L=[]
  startstate=3  #startzustand
  L.append(startstate)
  currentstate=3
  for i in (1..itnum) do
    currentstate=step(currentstate) #ermittelt nächsten Zustand
    L.append(currentstate)
    
  end
  return L
  
end

print(walk(20))


in_thread do  #definiere Tonspur
  loop do     #folgende Sequenz wird in Dauerschleife abgespielt
    sample:drum_snare_hard  #Schlagzeug
    sleep 0.5
    sample:bd_haus
    sleep 0.5
    sample:bd_haus
    sleep 0.75
    sample:bd_haus
    sample:drum_snare_hard
    sleep 0.75
    sample:drum_snare_hard
    sleep 0.5
    sleep 0.5
    sample:bd_haus
    sleep 1
  end
end

in_thread do
  G.each do|j| #jedem Zustand wird ein Ton zugeordnet, es wird über die Liste iteriert...
    if j==4
      play:C,release:0.75 #release: wie lange wird Ton gespielt
      sleep 1
    end
    if j==3
      play:D,release:1.5
      sleep 1
    end
    if j==2
      play:G
      sleep 1
    end
    if j==1
      play:A,release:1.25
      sleep 1
    end
    if j==0
      play:B
      sleep 1
    end
  end
end
in_thread do  #Synthesizer
  use_synth:fm
  loop do
    
    use_synth :fm
    play 45,release:2
    sleep 1
    play 48,release:1.5
    sleep 1
    play 50,release:2
    sleep 1
    play 52,release:1.5
    sleep 2
  end
end



