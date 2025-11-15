from collections import deque
r, c = map(int, input().split())
space = [list(input()) for _ in range(r)]
q1 = deque()
q2 = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]

dist1 = [[-1]*c for i in range(r)]
dist2 = [[-1]*c for i in range(r)]

flag = 0
for i in range(r):
    for j in range(c):
        if space[i][j] == 'J':
            q1.append((i, j))
            dist1[i][j] = 0
        elif space[i][j] == 'F':
            q2.append((i, j))
            dist2[i][j] = 0

while q2:
    x, y = q2.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if space[nx][ny] != '#' and dist2[nx][ny] == -1:
            dist2[nx][ny] = dist2[x][y] + 1
            q2.append((nx, ny))

while q1:
    x, y = q1.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            print(dist1[x][y] + 1)
            flag = 1
            break
        if space[nx][ny] != '#' and dist1[nx][ny] == -1:
            if (dist1[x][y] + 1) < dist2[nx][ny] or dist2[nx][ny] == -1:
                dist1[nx][ny] = dist1[x][y] + 1
                q1.append((nx, ny))
    if flag:
        break

if not flag:
    print("IMPOSSIBLE")
