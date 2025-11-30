from collections import deque
n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]

dist =[[-1] * n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
a = 0
arrs = []
for i in range(n):
    for j in range(n):
        if space[i][j] == 1 and dist[i][j] == -1:
            q = deque([(i,j)])
            dist[i][j] = 0
            a += 1
            arr = [(i,j)]
            space[i][j] = a
            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx,ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if space[nx][ny] == 1 and dist[nx][ny] == -1:
                        space[nx][ny] = a
                        dist[nx][ny] = 0
                        q.append((nx,ny))
                        arr.append((nx,ny))
            arrs.append(arr)
        
min_count = int(1e9)
        
for i in range(len(arrs)):
    dist = [[-1] * n for _ in range(n)]
    q2 = deque()
    count = 0
    flag = 0
    for x,y in arrs[i]:
        for j in range(4):
            nx,ny = x + dx[j], y + dy[j]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if space[nx][ny] == 0:
                q2.append((x,y))
                dist[x][y] = 0
                break
    while q2:
        x,y = q2.popleft()
        
        for j in range(4):
            nx,ny = x + dx[j], y + dy[j]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if space[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q2.append((nx,ny))
            if space[nx][ny] != i+1 and space[nx][ny] != 0:
                #print(x,y)
                count = dist[x][y]
                flag = 1
                break
        if flag == 1:
            break       
    
    # for k in range(n):
    #     print(dist[k])
    min_count = min (min_count,count)

print(min_count)