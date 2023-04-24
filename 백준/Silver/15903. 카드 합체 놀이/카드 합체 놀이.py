#아이디어
#가장 작은 카드 두장만을 계속 골라 합친다

#heapq에 넣고 pop으로 최소인 카드 2장을 뽑은 뒤 합친다
#합친 카드값을 push로 2번 넣는다
#위 과정을 m번 반복한다

import sys
import heapq
input=sys.stdin.readline

n,m=map(int,input().split())
data=list(map(int,input().split()))

#heqpq에 카드 값 넣기
q=[]
for i in data:
  heapq.heappush(q,i)

#m번 반복,최솟값 카드 2장 뽑고 카드 값 합친 후 heapq에 2장 넣기
for i in range(m):
  a=heapq.heappop(q)
  b=heapq.heappop(q)
  #합한 값을 카드에 덮어쓰므로 2장을 다시 넣는다
  heapq.heappush(q,a+b)
  heapq.heappush(q,a+b)

result=sum(q)
print(result)