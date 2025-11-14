from collections import deque

n, m = map(int, input().split())
space = [list(input()) for _ in range(n)]

# 방향 벡터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# dist[x][y][0] = 벽을 안 부수고 방문
# dist[x][y][1] = 벽을 부수고 방문
dist = [[[ -1 ] * 2 for _ in range(m)] for __ in range(n)]

# BFS 초기화 (0,0)에서 시작, 아직 벽을 안 부쉈으므로 flag = 0
q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

while q:
    x, y, w = q.popleft()

    # 도착하면 바로 출력
    if x == n - 1 and y == m - 1:
        print(dist[x][y][w])
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 빈 칸인 경우 → 현재 w 상태 그대로 이동 가능
        if space[nx][ny] == '0' and dist[nx][ny][w] == -1:
            dist[nx][ny][w] = dist[x][y][w] + 1
            q.append((nx, ny, w))

        # 벽인데 → 아직 벽을 안 부순 상태(w == 0)라면 부술 수 있음
        elif space[nx][ny] == '1' and w == 0 and dist[nx][ny][1] == -1:
            dist[nx][ny][1] = dist[x][y][0] + 1
            q.append((nx, ny, 1))

else:
    # break 없이 끝났다면 도착 못 함
    print(-1)
