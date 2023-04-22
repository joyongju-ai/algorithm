#내 풀이
from collections import deque
tc=int(input())

for _ in range(tc):
  n=int(input())
  data=list(map(int,input().split()))
  
  prices=[]  #가격,날짜 저장
  #data를 살펴보며 가격 날짜 저장@
  for i in range(len(data)):
    prices.append((data[i],i))

  #가격 내림차순,날짜 오름차순으로 정렬
  prices.sort(key=lambda x: (-x[0],x[1]))
  
  start=0         #시작 날짜
  profit=0        #주식 판 이익
  

  for i in range(len(prices)):
    #탐색 후 제거하므로 price[0]만 뽑아도 된다@
    #만약 뽑은 날짜가 start이후라면
    if prices[i][1]>=start:
      gap=prices[i][1]-start
      #start부터 뽑은 날짜 이전까지 주식 매입
      #뽑은 가격에 팔아서 생긴 이익을 추가
      profit+=prices[i][0]*(gap)-(sum(data[start:prices[i][1]]))
      #start 뽑은 날짜+1로 갱신@
      start=prices[i][1]+1
            
  print(profit)