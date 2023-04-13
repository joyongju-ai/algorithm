from collections import deque
n,k=map(int,input().split())
INF=int(1e9)
visited=[False]*(100001)
distance=[INF]*(100001)

q=deque([n])
visited[n]=True
distance[n]=0

while q:
  now=q.popleft()

  if now+1<100001 and not visited[now+1]:
    q.append(now+1)
    distance[now+1]=distance[now]+1
    visited[now+1]=True
  if now-1>=0 and not visited[now-1]:
    q.append(now-1)
    distance[now-1]=distance[now]+1
    visited[now-1]=True
  if now*2<100001 and not visited[now*2]:
    q.append(now*2)
    distance[now*2]=distance[now]+1
    visited[now*2]=True
  if visited[k]:
    break
    
print(distance[k])