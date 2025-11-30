import sys
sys.setrecursionlimit(10**5)

def dfs(x):
    global cnt
    visited[x] = True
    nx = arr[x]

    if not visited[nx]:
        dfs(nx)
    elif not finished[nx]:
        # 사이클 발견
        cur = nx
        cycle_len = 1
        while arr[cur] != nx:
            cur = arr[cur]
            cycle_len += 1
        cnt += cycle_len

    finished[x] = True


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n+1)
    finished = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(n - cnt)
