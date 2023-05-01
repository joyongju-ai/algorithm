n=int(input())

dp=[0]*(n+1)

dp[1]=3
#n이 1일 때 dp[2]는 없으므로 2이상 부터만 
if n>=2:
  dp[2]=7

for i in range(3,n+1):
  dp[i]=(dp[i-1]*2+dp[i-2])%9901
  
print(dp[-1])