from collections import deque
m,n,h = map(int,input().split())
space = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
dist = [[[-1]*m for _ in range(n)] for _ in range(h)]
q = deque()

d = [(0,0,1),(0,1,0),(0,0,-1),(0,-1,0),(1,0,0),(-1,0,0)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if dist[i][j][k] == -1 and space[i][j][k] == 1:
                q.append((i,j,k))
                dist[i][j][k] = 0

while q:
    k,x,y = q.popleft()

    for i in range(6):
        nk,nx,ny = k + d[i][0], x + d[i][1], y + d[i][2]

        if nk < 0 or nk >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nk][nx][ny] == -1 and space[nk][nx][ny] == 0:
            dist[nk][nx][ny] = dist[k][x][y] + 1
            q.append((nk,nx,ny))

flag = 1
days = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if dist[i][j][k] == -1 and space[i][j][k] != -1:
                flag = 0
            else:
                days = max(days, dist[i][j][k])

if flag:
    print(days)
else:
    print(-1)