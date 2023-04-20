#동전0
#백준 11047
#모든 동전이 배수-작은 동전의 합이 무조건 큰 동전
#무조건 큰 동전을 먼저 많이 사용하는게 유리->그리디

n,k=map(int,input().split())
coins=[]
for i in range(n):
  coins.append(int(input()))

count=0    #동전 수
#k가 0이 될 때까지
while k:
  result=0  #k보다 작은 가장 큰 동전
  #k보다 작은 가장 큰 동전 찾기
  for i in range(len(coins)):
    if k>=coins[i]:
      result=max(result,coins[i])
  #k가 동전보다 작아질 때까지 빼주고 count 추가
  while k>=result:
    k-=result
    count+=1
    
print(count)