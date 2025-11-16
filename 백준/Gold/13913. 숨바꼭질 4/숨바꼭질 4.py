from collections import deque

n, k = map(int, input().split())

q = deque([(n,-1)])
dist = [[-1]*2 for _ in range(100001)]
dist[n][0] = 0

while q:
    x, prev = q.popleft()
    if x == k:
        print(dist[k][0])
        break

    for dx in [1, -1, x]:  # 2x 표현하기 위해 x를 더했다.
        nx = x + dx
        # 이 부분이 위에서 말한 왜 범위를 이렇게 생각해야 하는지 생각하라는 부분이다.
        # 범위의 정당성을 생각하고 이렇게 해야 한다.
        if nx < 0 or nx > 100000:
            continue
        if dist[nx][0] == -1:
            dist[nx][0] = dist[x][0] + 1
            dist[nx][1] = x
            q.append((nx,x))

path = [k]

while True:
    if path[-1] == -1:
        break
    path.append(dist[path[-1]][1])

path.reverse()
path = path[1:]
print(*path)