import sys
sys.setrecursionlimit(10**5)   # 재귀깊이 996에서 10만까지 확대

def dfs(x):
    global cnt
    visited[x] = True
    team.append(x)
    nx = arr[x]
    
    if visited[nx]:
        if nx in team:
            cnt += len(team[team.index(nx):])
    else:
        dfs(nx)


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [False] * (n+1)       #방문 여부 확인
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(n - cnt)