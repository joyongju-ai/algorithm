from collections import deque

f,s,g,u,d = list(map(int,input().split()))

dist = [-1] * (f+1)
q = deque([s])
dist[s] = 0

while q:
    x = q.popleft()

    for nx in [x+u,x-d]:
        if nx < 1 or nx > f:
            continue
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

if dist[g] != -1:
    print(dist[g])
else:
    print("use the stairs")