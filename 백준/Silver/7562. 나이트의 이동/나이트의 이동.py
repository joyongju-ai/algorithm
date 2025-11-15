from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    dist = [[-1] * n for _ in range(n)]
    start = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))
    q = deque([start])
    d = [(-1,2),(1,2),(-2,1),(-2,-1),(2,1),(2,-1),(-1,-2),(1,-2)]
    dist[start[0]][start[1]] = 0

    while q:
        x,y = q.popleft()
        if x == end[0] and y == end[1]:
            print(dist[x][y])
            break

        for i in range(8):
            nx,ny = x + d[i][0], y + d[i][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))