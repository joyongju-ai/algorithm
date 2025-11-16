from collections import deque
m,n,k = map(int,input().split())

space = [[0]*n for _ in range(m)]

#맵 직접생성
for i in range(k):
    y1,x1,y2,x2 = map(int,input().split())
    for row in range(m -x2, m - x1):
        for col in range(y1, y2):
            space[row][col] = 1

dist = [[-1]*n for _ in range(m)]
q = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]

count = 0
areas = []
for i in range(m):
    for j in range(n):
        if space[i][j] == 0 and dist[i][j] == -1:
            count += 1
            q.append((i,j))
            dist[i][j] = 1
            area = 1
            while q:
                x,y = q.popleft()

                for k in range(4):
                    nx,ny = x + dx[k], y +dy[k]
                    if nx < 0 or nx >= m or ny <0 or ny >= n:
                        continue
                    if space[nx][ny] == 0 and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx,ny))
                        area += 1
            areas.append(area)

areas.sort()
print(count)
print(*areas)