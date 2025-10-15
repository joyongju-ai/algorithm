n,m = list(map(int,input().split()))
x,y,d = list(map(int,input().split()))

g_map = []
for i in range(n):
    g_map.append(list(map(int, input().split())))

g_map[x][y] = 2 
moves = [(-1,0),(0,1),(1,0),(0,-1)]

count = 0
result = 1
while(True):
    count += 1
    if count > 4:
        nx = x - moves[d][0]
        ny = y - moves[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if g_map[nx][ny] == 1:
            break
        x = nx
        y = ny
        count = 0
    else:
        d = (d+3)%4
        nx = x + moves[d][0]
        ny = y + moves[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if g_map[nx][ny] == 1 or g_map[nx][ny] == 2:
            continue
        if g_map[nx][ny] == 0:
            x = nx
            y = ny
            result += 1
            g_map[x][y] = 2
            count = 0
        
print(result)