#그리디
#시간이 적은 사람이 먼저 해야 뒷사람도 대기 시간이 줄어든다
#시간 적은 순대로 나열

n=int(input())

data=list(map(int,input().split()))

data.sort()

dp=[0]*(n+1)
result=0
for i in range(1,n+1):
  dp[i]=dp[i-1]+data[i-1]
  result+=dp[i]

print(result)