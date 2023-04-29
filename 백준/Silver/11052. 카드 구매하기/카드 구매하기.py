#아이디어
#카드 팩의 조합으로 1부터 카드 개수를 올려나간다
#카드 개수에 맞는 조합 중 가장 큰 비용을 dp에 저장한다
#구하는 카드 개수에서 카드 팩 카드 수를 뺀 인덱스의 dp값에 카드팩 비용을 더한다
#dp[i]=max(dp[i],dp[i-j-1]+prices[j])

#중요
#dp테이블 -1로 초기화,조합시 조합이 안되는 경우를 판단하기 유용한 기법,기억할 것

import sys

input=sys.stdin.readline
n=int(input())
prices=list(map(int,input().split()))

#dp테이블 -1로 초기화
dp=[-1]*(n+1)
dp[0]=0            #초깃값

#카드개수 1부터 올라가며
for i in range(1,n+1):
  #카드팩을 살펴보며
  for j in range(len(prices)):
    #카드팩 인덱스+1==카드 팩에 든 카드 수
    #구하는 카드 수보다 카드 팩 카드 수가 작거나 같을 때
    if i-(j+1)>=0:
      #이전의 조합이 가능하다면 거기에 현재 카드팩 값 더하기
      if dp[i-j-1]!=-1:
        #최댓값을 dp에 저장
        dp[i]=max(dp[i],dp[i-j-1]+prices[j])

print(dp[n])