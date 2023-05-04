#dp
#lis의 변형?
#dp는 입력값들로 초기화한다
#현재보다 작은 numbers를 찾고 그 중에서 가장 큰 dp값을 더해 dp 갱신

n=int(input())

numbers=list(map(int,input().split()))

dp=[]
for i in numbers:
    dp.append(i)

for i in range(1,n):
  result=0
  for j in range(i):
    if numbers[i]>numbers[j]:
      result=max(result,dp[j])
  dp[i]+=result

print(max(dp))