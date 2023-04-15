from pprint import pprint

dx=[0,1,0,-1]
dy=[1,0,-1,0]

n=int(input())

k=int(input())
apple=[]
array=[]
for i in range(k):
  array=list(map(int,input().split()))
  apple.append(array)

rotate=[]
l=int(input())
for i in range(l):
  x,y=input().split()
  rotate.append([int(x),y])
  
field=[[0]*n for _ in range(n)]

visited=[[0]*n for _ in range(n)]
visited[0][0]=1

for i in apple:
  x,y=i
  field[x-1][y-1]=1

time=0
x=0
y=0
direction=0
length=1
position=[]
while True:
  time=time+1
  for i,j in rotate:
    if time-1==i:
      if j=="L":
        direction-=1
        if direction == -1:
          direction=3
          
      elif j=="D":
        direction+=1
        if direction == 4:
          direction=0
          
  nx=x+dx[direction]
  ny=y+dy[direction]

  
  if 0<=nx<=n-1 and 0<=ny<=n-1 and visited[nx][ny]!=1:
    position.append([nx,ny])  
    visited=[[0]*n for _ in range(n)]
    visited[nx][ny]=1
    x=nx
    y=ny
    if field[nx][ny]==1:
      field[nx][ny]=0
      length+=1
      for pre_x,pre_y in position[-length:-1]:
        visited[pre_x][pre_y]=1
    
    else:
      for pre_x,pre_y in position[-length:-1]:
        visited[pre_x][pre_y]=1
   
  else:
    break
  
    
print(time)