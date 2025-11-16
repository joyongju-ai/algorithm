from collections import deque

n, k = map(int, input().split())

dist = [-1] * 100001
q = deque()
q.append(n)
dist[n] = 0

while q:
    x = q.popleft()

    if x == k:
        break

    # 비용 0: 순간이동
    if 0 <= 2*x <= 100000 and dist[2*x] == -1:
        dist[2*x] = dist[x]
        q.appendleft(2*x)   # ⬅️ 제일 앞에!

    # 비용 1: -1
    if 0 <= x-1 <= 100000 and dist[x-1] == -1:
        dist[x-1] = dist[x] + 1
        q.append(x-1)

    # 비용 1: +1
    if 0 <= x+1 <= 100000 and dist[x+1] == -1:
        dist[x+1] = dist[x] + 1
        q.append(x+1)

print(dist[k])
