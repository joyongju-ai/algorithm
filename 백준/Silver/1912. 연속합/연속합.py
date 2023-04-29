import sys

input=sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))

dp=[0]*n

for i in range(n):
  if i==0:
    dp[i]=numbers[i]
  else:
    if dp[i-1]<0:
      dp[i]=numbers[i]
    else:
      dp[i]=dp[i-1]+numbers[i]

print(max(dp))