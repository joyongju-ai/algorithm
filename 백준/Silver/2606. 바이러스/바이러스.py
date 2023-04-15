from collections import deque

n=int(input())
m=int(input())

#양방향 설정, 방향성 없었으므로
graph=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited=[False]*(n+1)
start=1

#bfs
q=deque([start])
visited[start]=True
count=0      #1에 의해 감염된 컴퓨터 수
while q:
  now=q.popleft()
  
  for i in graph[now]:
    if not visited[i]:
      q.append(i)
      visited[i]=True
      count+=1

print(count)