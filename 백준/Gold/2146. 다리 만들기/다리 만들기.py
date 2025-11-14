from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.appendleft((x, y))
    graph[x][y] = tmp
    while q:
        x, y = q.pop()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if not(0 <= xx < n and 0 <= yy < n):
                continue
            if graph[xx][yy] != 1:
                continue
            graph[xx][yy] = tmp
            q.appendleft((xx, yy))

def bfs2(x, y, index):
    q = deque()
    q.appendleft((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if not(0 <= xx < n and 0 <= yy < n):
                continue
            if visited[xx][yy] != 0 or graph[xx][yy] == index:
                continue
            if graph[xx][yy] != index and graph[xx][yy] != 0:
                return visited[x][y] - 1
            q.appendleft((xx, yy))
            visited[xx][yy] = visited[x][y] + 1
    return 10 ** 10

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

tmp = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            tmp += 1

ans = 10 ** 10
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            visited = [[0] * n for _ in range(n)]
            ans = min(bfs2(i, j, graph[i][j]), ans)
print(ans)