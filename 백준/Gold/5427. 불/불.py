from collections import deque

T = int(input())

for _ in range(T):
    w,h = map(int,input().split())
    space = [list(input()) for _ in range(h)]
    dist1 = [[-1]*w for _ in range(h)]
    dist2 = [[-1]*w for _ in range(h)]

    q1 = deque()
    q2 = deque()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    flag = 0

    for row in range(h):
        for col in range(w):
            if space[row][col] == '@':
                q1.append((row,col))
                dist1[row][col] = 0
            elif space[row][col] == '*':
                q2.append((row,col))
                dist2[row][col] = 0

    while q2:
        x,y = q2.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if space[nx][ny] != '#' and dist2[nx][ny] == -1:
                dist2[nx][ny] = dist2[x][y] + 1
                q2.append((nx,ny))


    while q1:
        x,y = q1.popleft()

        for i in range(4):
            nx,ny = x + dx[i], y+dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                print(dist1[x][y] + 1)
                flag = 1
                break

            if space[nx][ny] == '.' and dist1[nx][ny] == -1:
                if (dist1[x][y] + 1) < dist2[nx][ny] or dist2[nx][ny] == -1:
                    dist1[nx][ny] = dist1[x][y] + 1
                    q1.append((nx,ny))

        if flag:
            break
    else:
        print("IMPOSSIBLE")