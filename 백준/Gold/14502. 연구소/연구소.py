from collections import deque
from itertools import combinations

n,m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]

viruses = []
visited = [[0]*m for _ in range(n)]
blanks = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for row in range(n):
    for col in range(m):
        if space[row][col] == 2:
            visited[row][col] = 2
            viruses.append((row,col))
        if space[row][col] == 1:
            visited[row][col] = 1
        if space[row][col] == 0:
            blanks.append((row,col))

max_count = -1
for comb in combinations(blanks,3):
    q = deque()
    for virus in viruses:
        q.append(virus)
    visited_copy = [[visited[x][y] for y in range(m)] for x in range(n)]

    for i,j in comb:
        visited_copy[i][j] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited_copy[nx][ny]:
                visited_copy[nx][ny] = 1
                q.append((nx,ny))
    count = 0
    for i in range(n):
        for j in range(m):
            if visited_copy[i][j] == 0:
                count += 1
    max_count = max(count, max_count)



print(max_count)