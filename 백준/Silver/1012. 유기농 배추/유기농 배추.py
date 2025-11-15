from collections import deque
T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())

    space = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for i in range(k):
        y,x = map(int,input().split())
        space[x][y] = 1

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    q = deque()
    bugs = 0
    for i in range(n):
        for j in range(m):
            if space[i][j] == 1 and visited[i][j] == 0:
                q.append((i,j))
                bugs += 1
                visited[i][j] = 1

                while q:
                    x,y = q.popleft()

                    for l in range(4):
                        nx, ny = x + dx[l] , y + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if space[nx][ny] == 1 and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx, ny))

    print(bugs)