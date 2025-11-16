from collections import deque
while True:
    l,r,c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    space = []
    for k in range(l):
        temp1 = []
        for i in range(r):
            temp = list(input())
            temp1.append(temp)
        a = input()
        space.append(temp1)

    q = deque()
    d = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    dist = [[[-1] * c for _ in range(r)] for _ in range(l)]

    for height in range(l):
        for row in range(r):
            for col in range(c):
                if space[height][row][col] == 'S':
                    q.append((height,row,col))
                    dist[height][row][col] = 0

    while q:
        h,x,y = q.popleft()

        if space[h][x][y] == 'E':
            print(f"Escaped in {dist[h][x][y]} minute(s).")
            break
        for i in range(6):
            nh,nx,ny = h + d[i][0], x + d[i][1], y + d[i][2]

            if nh < 0 or nh >= l or nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if space[nh][nx][ny] != '#' and dist[nh][nx][ny] == -1:
                dist[nh][nx][ny] = dist[h][x][y] + 1
                q.append((nh,nx,ny))
    else:
        print("Trapped!")