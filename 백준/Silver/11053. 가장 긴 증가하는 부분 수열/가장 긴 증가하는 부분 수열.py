#dp
#전형적인 dp문제
#lis

n=int(input())

numbers=list(map(int,input().split()))

dp=[1]*1000

for i in range(1,n):
  for j in range(i):
    if numbers[i]>numbers[j]:
      dp[i]=max(dp[i],dp[j]+1)


print(max(dp))