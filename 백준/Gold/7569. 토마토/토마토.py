#아이디어 
#중요한 것은 기존의 모든 좌표 조사와 달리 필요한 좌표만 deque인 next에 넣고 꺼내어 bfs를 사용한 것이다->시간이 덜 걸린다
#즉 deque를 bfs실행하는 데에만 쓰는 것이 아니라 필요한 좌표를 선입선출할 때 사용한 것이 주요한 아이디어이다==deque를 2개 사용했다
#리스트를 사용한다면 선입선출이 오래 걸리고 선입선출을 만약 하지 않는다면 조사하는데 시간이 오래 걸린다==deque 사용하면 해결

from collections import deque
import sys

input=sys.stdin.readline

m,n,h=map(int,input().split())

#입력값 받기+ 값이 1인 그래프 좌표 deque에 넣기
next=deque()
graph=[[] for _ in range(h)]
for i in range(h):
  for j in range(n):
    graph[i].append(list(map(int,input().split())))
    for k in range(m):
      if graph[i][j][k]==1:  #익은 토마토만 next에 넣기
        next.append((i,j,k))

#방향 벡터
dx=[0,1,0,-1,0,0]
dy=[1,0,-1,0,0,0]
dz=[0,0,0,0,1,-1]

#bfs로 1회 6방향 살펴보며 조건에 맞으면 기존 graph값+1을 새로운 graph에
#대입하고 next에 해당 좌표를 추가하는 함수
def bfs(a,b,c):
  q=deque([(a,b,c)])   #입력값 deque에 넣기
  x,y,z=q.popleft()    #빼기
  for i in range(6):   #6방향 조사
    nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]  
    if not(0<=nx<n and 0<=ny<m and 0<=nz<h):  #리스트 범위 초과시
      continue
    if graph[nz][nx][ny]!=0:#이전에 방문했거나 토마토가 없는 경우
      continue
    graph[nz][nx][ny]=graph[z][x][y]+1  #기존값 +1을 대입
    next.append((nz,nx,ny))  #next에 다음에 살펴볼 좌표를 대입
  return

#next에서 하나씩 꺼내 bfs 실행
#next가 빈다면 더이상 살펴봐야할 좌표가 없다는 뜻이므로 종료
while next:
  z,x,y=next.popleft()
  bfs(x,y,z)

#graph 체크하며 0있는지 확인 있다면 익지 않은 토마토 있다는 뜻, result로 graph[z][x][y] 최댓값 구하기
result=1
for z in range(h):
  for x in range(n):
    for y in range(m):
      if graph[z][x][y]==0:
        result=int(1e9)      #0인 경우 result를 매우 큰 값으로
      else:
        result=max(result,graph[z][x][y])


if result!=int(1e9):
  print(result-1)
else:
  print(-1)