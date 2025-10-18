import sys
input = sys.stdin.readline
n, m = list(map(int,input().rstrip().split()))

coins = []
for i in range(n):
    coins.append(int(input().rstrip()))
inf = 1e9

dp = [inf]* 100001
dp[0] = 0

for i in coins:
    dp[i] = 1

for i in range(m+1):
    for j in coins:
        if i >= j:
            dp[i] = min(dp[i],dp[i-j]+1)

if dp[m] == inf:
    print(-1)
else:
    print(dp[m])