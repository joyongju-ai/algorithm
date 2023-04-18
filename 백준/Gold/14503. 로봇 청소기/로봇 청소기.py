n,m=map(int,input().split())

x,y,d=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

visited=[[0]*m for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y,d):
  #print(visited)
  if graph[x][y]==1:
    return 
  visited[x][y]=2
  for i in range(4):
    d=d-1
    if d==-1:
      d=3
    #print(d)
    nx=x+dx[d]
    ny=y+dy[d]
    if not(0<=nx<n and 0<=ny<m):
      continue
    if graph[nx][ny]==1 or visited[nx][ny]!=0:
      continue
    return dfs(nx,ny,d)
  return dfs(x-dx[d],y-dy[d],d)

    
dfs(x,y,d)
count=0
for i in range(n):
  for j in range(m):
   if visited[i][j]==2:
     count+=1

print(count)