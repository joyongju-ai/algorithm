n=int(input())
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

dp=[0]*(n+1)

for i in range(n):
  if (n-1-i+(data[n-1-i][0]-1))<n:
    result=data[n-1-i][1]+dp[n-1-i+data[n-1-i][0]]
    dp[n-1-i]=max(result,dp[n-i])
  else:
    dp[n-1-i]=dp[n-i]

print(dp[0])