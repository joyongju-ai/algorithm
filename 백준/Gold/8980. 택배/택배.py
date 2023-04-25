#그리디
#각 마을마다 트럭에 실린 박스를 교체,배달
#교체하는 경우는 트럭의 실린 박스 중 목적지가 가장 먼 것을 더 가까운 새 박스와 교체
#즉, 트럭에 실린 박스는 항상 목적지가 가장 가까운 것들로만 채워야 한다

#중요 
#heapq는 특정 원소를 제거하는 것이 어렵고 비효율적이다.
#나는 대신 박스 교체 시 박스 수 값을 줄여나가는 식으로 대체했다

#내 풀이
from collections import deque
import sys
import heapq

input=sys.stdin.readline

n,c=map(int,input().split())
m=int(input())

graph=[]
for i in range(m):
  graph.append(list(map(int,input().split())))

graph.sort()          #그래프 정렬

q=deque(graph)        #큐로 옮긴다

#print(q)
truck=[]    #현재 트럭에 들어있는 박스 현황
box=0       #트럭에 있는 박스 수
result=0    #배달한 박스 수
#마을을 순서대로 살펴보며
for vil in range(1,n+1):
  #print(vil)
  #print(truck)
  
  #트럭이 차 있고 목적지가 현재 마을이라면 반복
  while truck and truck[0][0]==vil:
    #해당 항을 뽑아 박스 배달
    a,delivered_box=heapq.heappop(truck)
    box-=delivered_box          #트럭 박스 배달한만큼 감소
    result+=delivered_box       #배달한 박스 수 증가 

  #q가 차있고 출발지가 현재 마을이라면 반복,적절한 박스로 채우기
  while q and q[0][0]==vil:
    start,end,count=q.popleft()
    temp_count=count  #임시 박스 수 
    #truck을 역순으로 확인하며 목적지가 더 먼 박스가 있으면 내리기
    for i in range(len(truck)-1,-1,-1):
      #목적지가 더 먼 박스가 있다면 내린다
      if truck[i][0]>end:
        #만약 임시 박스 수가 내리는 박스 수보다 많으면 
        if temp_count>truck[i][1]:
          temp_count-=truck[i][1]    #임시 박스를 내리는 박스 수 만큼 줄임
          box-=truck[i][1]    #현재 트럭에 실린 박스는 내리는 만큼 줄임
          #트럭에 실린 박스 수를 0으로 바꾼다 
          #힙에서 특정원소 제거는 어려우므로 
          truck[i][1]=0            
        #더 적다면 임시박스만큼 박스를 내린다
        else:
          box-=temp_count        #현재 박스 수를 임시박스만큼 내린다
          truck[i][1]-=temp_count  #내리는 박스를 임시박스만큼 내린다
          temp_count=0             #임시박스는 0으로 
          
    #현재 박스 수+새 박스 수가 용량 이내이면
    if box+count<=c:
      #truck에 [목적지,새로 넣는 박스 수] 추가
      heapq.heappush(truck,[end,count])  
      box+=count      #트럭 내 박스 수 증가
    #용량 초과 시 용량 될 때까지만 박스 넣기
    else:
      heapq.heappush(truck,[end,c-box])  #[목적지,가능한 박스 수]
      box=c    #현재 트럭 내에 실린 박스는 용량만큼이므로
        
  #print(result)
  #print()
print(result)