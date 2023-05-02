#계단 오르기
#2549

n=int(input())

stairs=[]
for i in range(n):
  stairs.append(int(input()))


if n>=2:
  dp=[[0,stairs[0]],[stairs[1],stairs[0]+stairs[1]]]

for i in range(2,n):
  a=max(dp[i-2])
  b=dp[i-1][0]
  c=dp[i-1][1]
  stair=stairs[i]
  array=[a+stair,b+stair]
  dp.append(array)



if n==1:
  print(stairs[0])
elif n==2:
  print(stairs[0]+stairs[1])
else:
  print(max(dp[n-1][0],dp[n-1][1]))