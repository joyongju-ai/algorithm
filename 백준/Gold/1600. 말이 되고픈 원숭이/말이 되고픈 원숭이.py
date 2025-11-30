from collections import deque
k = int(input())
w,h = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(h)]

dist = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]
dx = [0,1,0,-1,-1,1,2,2,1,-1,-2,-2]
dy = [1,0,-1,0,2,2,1,-1,-2,-2,-1,1]

q = deque([(0,0,0)])
dist[0][0][0] = 0

while q:
    x,y,count = q.popleft()
    if (x,y) == (h-1,w-1):
        print(dist[x][y][count])
        break
    
    for i in range(12):
        nx,ny = x + dx[i], y + dy[i]
        if i >=4 and count >= k:
            continue
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if i <= 3:
            if space[nx][ny] == 0 and dist[nx][ny][count] == -1:
                dist[nx][ny][count] = dist[x][y][count] + 1
                q.append((nx,ny,count))
        if i >= 4 :
            if space[nx][ny] == 0 and dist[nx][ny][count+1] == -1:
                dist[nx][ny][count+1] = dist[x][y][count] + 1
                q.append((nx,ny,count+1))
else:
    print(-1)