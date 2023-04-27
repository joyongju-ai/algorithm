#아이디어
#2차원 배열을 그대로 dp로 활용,갱신
#각 점을 목적지로 생각하고 세 방향에서 모이는 점이라고 생각한다.
#즉 한 점에서 세 방향으로 퍼지는 것을 거꾸로 생각해 한 점으로 모인다고 생각 
#graph[i][j]+=max(graph[i][j-1],graph[i-1][j],graph[i-1][j-1])

#내 풀이
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

#각 점에 대해 세 방향중 가장 사탕이 많은 쪽을 더한다
#처음에 갱신이 제대로 되나 걱정했지만 이 순서로 하면 문제 없다
for i in range(n):
  for j in range(m):
    if i>0 and j>0:
      #점화식
      graph[i][j]+=max(graph[i][j-1],graph[i-1][j],graph[i-1][j-1])
    elif i==0 and j>0:  #미로 밖으로 못 나가게 설정
      graph[i][j]+=graph[i][j-1]
    elif i>0 and j==0:  #미로 밖으로 못 나가게 설정
      graph[i][j]+=graph[i-1][j]

print(graph[n-1][m-1])