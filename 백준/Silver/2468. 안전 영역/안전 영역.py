from collections import deque
from copy import deepcopy
n=int(input())

field=[]
for i in range(n):
  field.append(list(map(int,input().split())))
copyfield=deepcopy(field)

max_height=0
min_height=101
for i in range(n):
  for j in range(n):
    max_height=max(max_height,field[i][j])
    min_height=min(min_height,field[i][j])

def bfs(start,height):
  q=deque([start])
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n:
        if field[nx][ny]>height:
          field[nx][ny]=0
          q.append((nx,ny))


count=0
result=[]
for k in range(min_height,max_height+1):
  for i in range(n):
    for j in range(n):
      if field[i][j]>k:
        count+=1
        bfs((i,j),k)
  result.append(count)
  count=0
  field=deepcopy(copyfield)

if max(result)==0:
  print(1)
else:
  print(max(result))