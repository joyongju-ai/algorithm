n=int(input())
dp=[]
for i in range(n):
  dp.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(n-i):
    dp[n-1-i][j]+=max(dp[n-1-i+1][j],dp[n-1-i+1][j+1])

print(dp[0][0])