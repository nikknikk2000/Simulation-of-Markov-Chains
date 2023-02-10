P=[[0,6,0,0,0],[0,0,6,0,0],[0,0,0,6,0],[2,2,0,0,2],[3,0,0,0,3]]


define:step do |i|  #step macht einen Iterationsschritt, gibt zustand zurück
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
  L=[3]  #Startzustand des ersten Walks:3
  M=[4]  #Startzustand des zweiten Walks:4
  currentstate1=1
  currentstate2=4
  while currentstate1!=currentstate2 do
    currentstate1=step(currentstate1) #ermittelt nächsten Zustand
    L.append(currentstate1)
    currentstate2=step(currentstate2)
    M.append(currentstate2)
  end
  return L,M
end

print(walk(1))

L,M=walk(10)


in_thread do
  L.each do|j|
    if j==4
      play:C
      sleep 1
    end
    if j==3
      play:D
      sleep 1
    end
    if j==2
      play:G
      sleep 1
    end
    if j==1
      play:A
      sleep 1
    end
    if j==0
      play:B
      sleep 1
    end
  end
end



in_thread do
  M.each do|j|
    if j==4
      play:C
      sleep 1
    end
    if j==3
      play:D
      sleep 1
    end
    if j==2
      play:G
      sleep 1
    end
    if j==1
      play:A
      sleep 1
    end
    if j==0
      play:B
      sleep 1
    end
  end
end







