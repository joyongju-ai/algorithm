from collections import deque
n = int(input())
space = [list(input()) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()
count1 = 0
count2 = 0
for row in range(n):
    for col in range(n):
        if visited[row][col] == 0:
            visited[row][col] = 1
            q.append((row, col))
            target = space[row][col]
            count1 += 1
            while q:
                x,y = q.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if space[nx][ny] == target and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

visited = [[0]*n for _ in range(n)]

for row in range(n):
    for col in range(n):
        if visited[row][col] == 0:
            visited[row][col] = 1
            q.append((row, col))
            target = space[row][col]
            count2 += 1
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if visited[nx][ny] == 0:
                        if target == 'R' or target == 'G':
                            if space[nx][ny] == 'R' or space[nx][ny] == 'G':
                                visited[nx][ny] = 1
                                q.append((nx, ny))
                        elif target == 'B':
                            if space[nx][ny] == target:
                                visited[nx][ny] = 1
                                q.append((nx,ny))

print(count1, count2)