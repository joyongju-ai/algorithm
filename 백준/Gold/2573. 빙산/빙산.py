from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]
    count = 1
    q = deque()
    q.append(ice[0])
    visited[ice[0][0]][ice[0][1]] = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if space[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                count += 1
    #print(count,len(ice))
    if count != len(ice):
        return 1
    else:
        return 0


n,m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]


q = deque()
ice = []
for i in range(n):
    for j in range(m):
        if space[i][j] != 0:
            ice.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

year = 0
while True:
    year += 1
    decrease = []
    for x,y in ice:
        dec = 0
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if space[nx][ny] == 0:
                dec += 1
        decrease.append(dec)
    #print(decrease)
    for i in range(len(ice)):
        space[ice[i][0]][ice[i][1]] -= decrease[i]
        if space[ice[i][0]][ice[i][1]] <= 0:
            space[ice[i][0]][ice[i][1]] = 0
    for i in range(len(ice)-1,-1,-1):
        if space[ice[i][0]][ice[i][1]] == 0:
            #print(ice[i][0],ice[i][1])
            ice.pop(i)
    #print(ice)
    if ice:
        result = bfs()
        if result == 1:
            print(year)
            break
        #else:
        #   print("실패")
    else:
        print(0)
        break