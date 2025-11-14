from collections import deque

m, n = map(int, input().split())
space = [list(map(int, input().split())) for i in range(n)]
dist = [[-1]*m for i in range(n)]

q = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] == -1 and space[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

flag = 1
days = 0
for i in range(n):
    for j in range(m):
        if space[i][j] != -1 and dist[i][j] == -1:
            flag = 0
        days = max(days, dist[i][j])

if flag == 1:
    print(days)
else:
    print(-1)