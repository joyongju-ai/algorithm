#순열사이클
#백준문제10451

#내 풀이
#추적하며 따라간다는 점에서 dfs와 유사
#dfs로 따라가다가 cycle이 형성되면 개수 1 증가
#dfs 재귀함수에서 결과값이 필요하면 return dfs, 필요없으면 그냥 dfs호출

#중요
#그래프 만들기,dfs

#내 풀이
#테스트 케이스 수
t=int(input())

for _ in range(t):
  #입력부
  n=int(input())
  nums=list(map(int,input().split()))

  #그래프 만들기
  graph=[[]*(n+1) for i in range(n+1)]
  #입력받은 값을 1~n과 간선으로 연결,1-nums[0],2-nums[1]의 형식으로 
  for i in range(1,n+1):
    graph[i].append(nums[i-1])
    
  #방문기록 만들기
  visited=[False]*(n+1)

  cycle=0  #사이클 개수 변수

  
  #dfs, #graph[start]로 하려했는데 리스트라 안된다고 해서 graph[start][0]로 함
  def dfs(graph,start,visited,target):
    visited[start]=True
    #graph가 가리키는 값이 target값이라면 True 반환,cycle 형성
    if graph[start][0]==target:
      return True
    #graph 가리키는 값이 미방문 노드라면
    if not visited[graph[start][0]]:
      #재귀함수로 추적
      return dfs(graph,graph[start][0],visited,target)

      
  #1부터 순열을 확인하며
  for i in range(1,n+1):
    #만약 방문하지 않았다면,사이클이 아직 만들어지지 않았다는 의미
    if not visited[i]:
      #dfs로 사이클 추적,target은 사이클의 처음 시작 값인 i
      result=dfs(graph,i,visited,i)
      #사이클 있으면 1 증가
      if result==True:
        cycle+=1
        
  print(cycle)
  #방문기록 테스트 케이스 별로 초기화
  visited=[False]*(n+1)