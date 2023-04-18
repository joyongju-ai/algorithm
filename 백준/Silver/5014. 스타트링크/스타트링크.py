from collections import deque
f,start,goal,up,down=map(int,input().split()) 

distance=[0]*(f+1)

q=deque([start])
distance[start]=1

while q:
  now=q.popleft()

  for i in [now+up,now-down]:
    if not(1<=i<=f and distance[i]==0):
      continue
    distance[i]=distance[now]+1
    q.append(i)
  if distance[goal]>0:
    break

if distance[goal]==0:
  print("use the stairs")
else:
  print(distance[goal]-1)