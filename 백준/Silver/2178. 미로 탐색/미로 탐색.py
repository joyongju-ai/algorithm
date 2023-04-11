from collections import deque
#입력부
n,m=map(int,input().split())

#field 입력받기,공백으로 나눠주지 않았으므로 별도 처리
field=[]
for i in range(n):
  array=input()
  array=" ".join(array)
  field.append(list(map(int,array.split())))

#visited 초기화,start 초기화
visited=[[False]*(m) for i in range(n)]
start=(0,0)

#방향벡터
dx=[1,0,-1,0]
dy=[0,1,0,-1]


#bfs
def bfs(field,start,visited):
  q=deque([start])                  
  visited[start[0]][start[1]]=True
  
  while q:
    x,y=q.popleft()
    #4방향 살펴보며
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #미로를 벗어나지 않고
      if 0<=nx<n and 0<=ny<m:
        #미방문인 곳 중 field의 값이 1인 곳이면
        if field[nx][ny]==1 and not visited[nx][ny]:
          #field값을 이동 이전 노드의 값보다 1 높은 값으로 갱신
          field[nx][ny]=field[x][y]+1
          q.append((nx,ny))
          visited[nx][ny]=True
    #n-1,m-1에 도달하면 종료,최단거리 구하기 위해     
    if visited[n-1][m-1]==True:
      break
  return field[n-1][m-1]


print(bfs(field,start,visited))