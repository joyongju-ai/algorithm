# 실패 답지 보고 개조한 거임.
from collections import deque

# 사무실의 세로(N), 가로(M)
n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

# 남, 동, 북, 서 방향을 가리킴 (남쪽을 시작으로 반시계방향으로 돌아가는 순서로 되어 있음)
dy = [1, 0, -1, 0]  # y축
dx = [0, 1, 0, -1]  # x축

# 이 부분 생각못함.
# 감시해야하는 모든 방향 (각각의 cctv별로 감시할 수 있는 방향)
direction = {
    1: [[0], [1], [2], [3]],  # 1번cctv 방향:0, 1, 2, 3, --> 4가지
    2: [[0, 2], [1, 3]],  # 2번cctv 방향:(0, 2), (1, 3) --> 2가지
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번cctv 방향:(0, 1), (1, 2), (2, 3), (3, 0) --> 4가지
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번cctv 방향... 4가지
    5: [[0, 1, 2, 3]]  # 5번cctv 방향... 1가지
}

visited = [[0]*m for _ in range(n)]
cctv = []  # cctv의 위치를 저장할 큐
answer = 0
for i in range(n):
    for j in range(m):
        # 벽이아니고 빈칸이 아니면
        if space[i][j] != 6 and space[i][j] != 0:
            cctv.append((i, j))  # cctv번호, cctv 좌표 저장
            visited[i][j] = 1
        if space[i][j] == 6:
            visited[i][j] = 2
        # cctv가 아에 없는 경우도 고려해서 빈칸의 갯수로 맞춰둠
        if space[i][j] == 0:
            answer += 1

def move(x, y, direc, visit):
    # 각각의 방향에 대해서 전부 이동시켜줌
    for d in direc:
        nx,ny = x,y

        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어났거나 벽을 만났다면
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny] == 2:
                break
            # 빈칸이아니면
            else:
                visit[nx][ny] = 1


# 사각지대를 구하는 함수
def zero_cnt(visit):
    global answer
    cnt = 0
    for i in visit:
        cnt += i.count(0)
    answer = min(answer, cnt)


# 백준 15651 N과 M(3) 문제와 유사 (백트래킹)
def dfs(depth, visited):
    # space_copy = copy.deepcopy(space)
    visit = [[visited[x][y] for y in range(m)] for x in range(n)]
    # 2번째 상태가 실행되기전 바로 전 상태를 저장함
    # (예를 들어 2번째 상태를 시작하기 전에 1번째 상태의 결과를 저장함)
    if depth == len(cctv):
        zero_cnt(visited)
        return  # 전 상태로 돌아감

    x, y = cctv[depth]

    # number번째 cctv에 대해 가능한 모든 방향을 순차적으로 고려
    for d in direction[space[x][y]]:
        move(x, y, d, visit)
        dfs(depth + 1, visit)  # level+1번째 cctv를 고려
        visit = [[visited[x][y] for y in range(m)] for x in range(n)]
        # space_copy = copy.deepcopy(space)

        # 하나의 상태를 return 한다음 바로 전 상태로 바꿈
        # 만약 2번째 상태가 끝났다면,  1번째를 수행했을 때의 결과로 바꿈


dfs(0, visited)
print(answer)