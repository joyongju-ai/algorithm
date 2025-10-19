import sys
input = sys.stdin.readline

n,k = list(map(int,input().rstrip().split()))
dp=[[0]*7 for i in range(2)]
for i in range(n):
    sex,grade = list(map(int,input().rstrip().split()))
    dp[sex][grade] += 1

rooms = 0
for i in range(len(dp)):
    for j in range(len(dp[i])):
        if dp[i][j] %k != 0:
            rooms += dp[i][j] //k + 1
        else:
            rooms += dp[i][j] //k

print(rooms)