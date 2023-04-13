#내 식대로 개조한 코드
#즉석 리스트와 visted 배제에 초점
import sys
from collections import deque

MAX=10**5
INF=int(1e9)
distance=[INF]*(MAX+1)
n,k=map(int,sys.stdin.readline().split())

q=deque()
q.append(n)
distance[n]=0
while q:
    x=q.popleft()
    #즉석리스트
    for nx in (x-1,x+1,x*2):
        #distance 변형으로 방문처리 대신하기,visited 배제
        if 0 <= nx <= MAX and distance[nx]==INF:
            distance[nx]=distance[x]+1  
            q.append(nx)
    if distance[k]!=INF:
        break

print(distance[k])