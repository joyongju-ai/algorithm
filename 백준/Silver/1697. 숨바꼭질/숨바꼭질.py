from collections import deque
n,k = map(int,input().split())

q = deque([n])
dist= [-1]*100001
dist[n] = 0

while q:
    x = q.popleft()

    if x == k:
        print(dist[k])
        break
    for dx in [1,-1, x]:
        nx = x + dx
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)