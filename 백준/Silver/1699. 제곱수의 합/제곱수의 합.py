#dp,그리디와 헷갈리지 않게 주의
#동전조합류 문제
#뭘 조합해서 최소 최대 만들라는 케이스

#아이디어
#1부터 올린다
#각각 최소의 제곱수 항 개수를 dp에 저장한다
#구하려는 수가 제곱수보다 작으면 제곱수를 뺀 경우의 조합이 있다면 개수를 1 추가한다
#실행시간 줄이기 위해 제곱근만큼 제곱수를 만들었다

import math
n=int(input())

#제곱수 배열,1^2부터 (루트n)^2까지 만든다
#소수점 뒷자리는 int하면 버림된다
square=[]
for i in range(1,int(math.sqrt(n))+2):
  square.append(i**2)

#dp 테이블 초기화 
dp=[10001]*(n+1)
dp[0]=0          #초깃값

#1부터 올려가며
for i in range(1,n+1):
  #제곱수를 살펴보며
  for j in square:
    if i>=j:
      #제곱수를 뺀 조합이 있다면
      if dp[i-j]!=10001:
        #개수를 1추가, 그 중 최소를 dp에 저장
        dp[i]=min(dp[i],dp[i-j]+1)

print(dp[n])