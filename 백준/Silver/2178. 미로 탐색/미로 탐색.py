#최단 경로는 bfs
import sys
from collections import deque
input = sys.stdin.readline

n,m = list(map(int,input().strip().split())) #readline에는 개행문자 들어감에 주의
maze = []
for i in range(n):
    temp = list(map(int,input().strip()))
    maze.append(temp)

visited=[[False]*m for _ in range(n)]

count_map = [[0]*m for _ in range(n)] #
start =(0,0)
goal = (n,m)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(maze, start, visited, goal ):
    queue = deque([start])
    visited[0][0] = True
    count_map[0][0] = 1
    n,m = goal
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            if not visited[nx][ny] and maze[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                count_map[nx][ny] = count_map[x][y] + 1 #
        if visited[n-1][m-1]:
            break
    return count_map[n-1][m-1]               
    
result = bfs(maze, start, visited, goal)
print(result)