#동전조합류 문제
#동전을 최소로 써서 조합하는 문제와 동전을 이용해 조합하는 모든 경우를 구하는 문제 중 후자에 해당
#순서만 바뀐 조합은 같은 것으로 본다

#아이디어
#화폐 단위만큼 빼준 dp값을 더한다->경우의 수 문제
#동전의 단위만큼 돌면서 dp갱신
#순서만 다른 같은 조합을 배제하기 위해

t=int(input())

for _ in range(t):
  #입력받기
  n=int(input())
  data=list(map(int,input().split()))
  target=int(input())

  #dp테이블 초기화
  dp=[0]*(target+1)
  dp[0]=1
  
  #동전별로 보면서
  for j in range(n):
    #동전보다 큰 경우 동전만큼 뺀 값을 더한다
    for i in range(1,target+1):
      if i>=data[j]:
        dp[i]+=dp[i-data[j]]

  print(dp[target])