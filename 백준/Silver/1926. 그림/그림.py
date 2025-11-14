from collections import deque
row, col = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(row)]
#print(space)
visited = [[0] * col for i in range(row)]

count = 0
max_size = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(row):
    for j in range(col):
        #print(i,j)
        if space[i][j] == 1 and not visited[i][j]:
            count += 1
            size = 0
            visited[i][j] = 1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                size += 1
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        continue
                    if visited[nx][ny] == 1 or space[nx][ny] == 0:
                        continue
                    visited[nx][ny] = 1
                    q.append((nx, ny))
            max_size = max(max_size, size)

print(count)
print(max_size)