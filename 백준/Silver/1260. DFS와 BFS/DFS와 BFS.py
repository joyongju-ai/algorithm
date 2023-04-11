#dfs 아직 부족, 더 공부해야 한다

from collections import deque

#입력부
n,m,start=map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)        

#양방향 간선정보 그래프에 넣기
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

#작은 정점부터 갈 수 있도록 정렬
for i in range(1,n+1):
  graph[i].sort()

#dfs
result1=[]
result1.append(start)
visited[start]=True          #출발 노드도 방문처리할 것
def dfs(start):
  for i in graph[start]:  
      if visited[i]==False:    #방문한 곳 재방문하지 않도록 설정
        result1.append(i)
        visited[i]=True
        dfs(i)
  return          #해당 노드에서 더 방문할 곳 없다면 종료

  
dfs(start)
for i in result1:
  print(i,end=" ")

print()
visited=[False]*(n+1)

#bfs
q=deque()
q.append(start)
visited[start]=True      #출발 노드도 방문처리할 것
result2=[]

while q:
  now=q.popleft()
  result2.append(now)
  
  for i in graph[now]:
    if visited[i]==False:    #방문한 곳 재방문하지 않도록 설정
        q.append(i)
        visited[i]=True

for i in result2:
  print(i,end=" ")
