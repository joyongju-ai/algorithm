from collections import deque

n, m = map(int, input().split())
maze = [list(input()) for i in range(n)]
dist = [[-1]*m for i in range(n)]

q = deque([(0, 0)])
dist[0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y = q.popleft()
    #print(x, y)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1 or maze[nx][ny] != '1':
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))

print(dist[n-1][m-1])