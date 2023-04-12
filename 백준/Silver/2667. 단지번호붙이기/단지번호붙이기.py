n=int(input())

field=[]
for i in range(n):
  array=input()
  array=" ".join(array)
  field.append(list(map(int,array.split())))

visited=[[False]*n for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]


def dfs(start,count):
  x,y=start
  visited[x][y]=True
  field[x][y]=count
  for k in range(4):
    nx=x+dx[k]
    ny=y+dy[k]
    if 0<=nx<n and 0<=ny<n:
      if field[nx][ny]==1 and visited[nx][ny]==False:
        dfs((nx,ny),count)
    
  
  
count=0
for i in range(n):
  for j in range(n):
    if field[i][j]==1 and visited[i][j]==False:
      start=(i,j)
      count+=1
      dfs(start,count)
      
print(count)

houses=[0]*(count+1)
for k in range(1,count+1):
    for i in range(n):
      for j in range(n):
        if field[i][j]==k:
          houses[k]+=1
houses.sort()
for i in houses[1:]:
  print(i)