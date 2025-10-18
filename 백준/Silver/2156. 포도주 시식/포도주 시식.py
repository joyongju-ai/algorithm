import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp = [0] * (n + 1)
    dp[1] = wine[0]
    dp[2] = wine[0] + wine[1]

    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + wine[i - 1],
            dp[i - 3] + wine[i - 2] + wine[i - 1]
        )

    print(dp[n])
