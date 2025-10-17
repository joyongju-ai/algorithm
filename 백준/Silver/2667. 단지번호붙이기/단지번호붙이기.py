import sys
input = sys.stdin.readline

n = int(input())

house_map =[]
for i in range(n):
    temp = list(input().strip())
    house_map.append(temp)
#print(ice_map)

visited= [[False]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(house_map,v,visited,house_pos):
    x,y = v
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and house_map[nx][ny] == '1':
            house_pos.append((nx,ny))
            dfs(house_map,(nx,ny),visited,house_pos)
    
count = 0
house_count =[]
for i in range(n):
    for j in range(n):
        house_pos =[] 
        i = int(i)
        j = int(j)
        if house_map[i][j] == '1' and not visited[i][j]:
            count += 1
            house_pos.append((i,j))
            dfs(house_map,(i,j),visited,house_pos)
            house_count.append(len(house_pos))
            
print(count)   
house_count.sort()
for i in house_count:
    print(i)