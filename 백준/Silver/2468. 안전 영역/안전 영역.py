from collections import deque

n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]

heights = []
for row in range(n):
    for col in range(n):
        if space[row][col] not in heights:
            heights.append(space[row][col])

q= deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]

max_count = 1

for h in heights:
    visited = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if space[i][j] > h and visited[i][j] == 0:
                q.append((i,j))
                visited[i][j] = 1
                count += 1
                while q:
                    x,y = q.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if nx < 0 or nx >= n or ny <0 or ny >= n:
                            continue
                        if space[nx][ny] > h and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx,ny))
    max_count = max(max_count, count)

print(max_count)