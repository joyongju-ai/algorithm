import sys
input = sys.stdin.readline

n = int(input().rstrip())
inf = 1e9

dp = [0]*1000001
for i in range(2,n+1):
    b,c,d = inf,inf,inf
    if i % 3 == 0:
        b = dp[i//3] + 1
    if i % 2 == 0:
        c = dp[i//2] + 1
    if i > 1:
        d = dp[i-1] + 1
    dp[i] = min(b,c,d)

print(dp[n])