from collections import deque
n, m, k = map(int, input().split())
maze = [list(input()) for i in range(n)]
dist = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y, w = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze[nx][ny] == '0' and dist[nx][ny][w] == -1:
            dist[nx][ny][w] = dist[x][y][w] + 1
            q.append((nx, ny, w))
        if maze[nx][ny] == '1' and w != k and dist[nx][ny][w+1] == -1:
            dist[nx][ny][w+1] = dist[x][y][w] + 1
            q.append((nx, ny, w+1))

flag = 0
min_dist = 1e9
for i in range(k+1):
    if dist[n-1][m-1][i] != -1:
        min_dist = min(min_dist, dist[n-1][m-1][i])
        flag = 1

if flag == 0:
    print(-1)
else:
    print(min_dist)