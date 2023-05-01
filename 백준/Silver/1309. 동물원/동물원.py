#dp
#타일 채우기 유형
#점화식 dp[i]=dp[i-1]*2+dp[i-2]
#메모리 초과 방지 위해 필요 없는 dp는 그때마다 pop

n=int(input())

dp=[0]*(n+1)

dp[1]=3
#n이 1일 때 dp[2]는 없으므로 2이상 부터만 
if n>=2:
  dp[2]=7
dp.pop(0)        #필요없으므로 pop

for i in range(3,n+1):
  dp[2]=dp[1]*2+dp[0]
  dp.pop(0)               #필요없으므로 pop
  
print(dp[-1]%9901)