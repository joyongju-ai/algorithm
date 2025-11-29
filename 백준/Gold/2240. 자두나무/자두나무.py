t,w = map(int,input().split())

plum = [0]+[int(input()) for _ in range(t)]
dp = [[[0]*(w+1) for _ in range(3)] for _ in range(t+1)]

dp[0][1][0] = 0
if plum[1] == 1:
    dp[1][1][0] = 1
else:
    dp[1][2][1] = 1

for i in range(2,t+1):
    if plum[i] == 1:
        dp[i][1][0] = dp[i-1][1][0] + 1
    elif plum[i] == 2:
        dp[i][1][0] = dp[i-1][1][0]
        
for i in range(2,t+1):
    for j in range(1,3):
        for k in range(1,i+1):
            if k > w:
                break
            dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][3-j][k-1])
            if plum[i] == j:
                dp[i][j][k] += 1

answer = -1
for i in range(1,3):
    for j in range(w+1):
        answer = max(answer,dp[t][i][j])

print(answer)