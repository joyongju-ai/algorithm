#내 풀이
#전형적인 플로이드 워셜 알고리즘 문제
#모든 도시에서 모든 다른 도시로의 최단 거리를 알아야 하므로

#중요
#간선 정보에서 같은 출발 같은 도착인데 비용만 다른 경우가 있었다, 이 경우 항상 거리가 작은 길로 가는 쪽이 거리가 짧으므로 거리가 짧은 쪽만 기록하도록 한다
#그래프 초기화 살짝 헷갈림

#입력부
import sys 
input=sys.stdin.readline
INF=int(1e9)
n=int(input())
m=int(input())

#graph 초기화,같은 도시에서 같은 도시로 이동하는 경우 거리 0으로 설정
graph=[[INF]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
  graph[i][i]=0

#간선 정보 받기
for i in range(m):
  a,b,c=map(int,input().split())
  #같은 출발,도착인데 비용만 다른 경우가 있다고 문제에서 명시, 최단 거리만 기록하기 위해
  graph[a][b]=min(graph[a][b],c)

#플로이드 워셜 알고리즘
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

#문제에서 도달 불가시 0으로 표시하라고 했기 때문에 INF를 0으로 바꿔줌
for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j]==INF:
      graph[i][j]=0

#결과 출력
for i in range(1,n+1):
  for j in range(1,n+1):
    print(graph[i][j],end=" ")
  print("")