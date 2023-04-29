#dp
#동전의 작은 단위의 배수가 항상 큰 단위가 되지 않는다->그리디 사용 불가->dp
#1부터 시작해 k까지올라가면서 화폐단위를 조합해 만들 수 있는 경우 최소 개수를 dp에 저장한다
#dp[i]=min(dp[i-j]+1) i는 인덱스,j는 화폐단위
#현재 인덱스에서 화폐를 뺀 값에 대한 조합이 있는지 확인하고 있다면 그중 최소를 택해 1을 더한다


n,k=map(int,input().split())

#화폐단위 저장
coins=[]
for i in range(n):
  coins.append(int(input()))

coins.reverse()

#dp테이블을 생길 수 있는 최대갯수+1인 10001로 초기화한다 
#k는 10000이 최대고 화폐단위는 1이 최소이므로 
dp=[10001]*(k+1)
dp[0]=0            #초깃값

#dp의 인덱스를 1씩 올라가면서 
for i in range(1,k+1):
  #만약 화폐단위보다 크거나 같은 인덱스이면 
  for j in coins:
    if i>=j:
      #화폐를 뺀 값에 대한 동전 조합이 있을 때
      if dp[i-j]!=10001:
        #그 중 최소+1이 dp[i],해당 동전을 더해야 하므로
        dp[i]=min(dp[i],dp[i-j]+1)

#dp[k]의 조합이 없으면 -1
if dp[k]==10001:
  print(-1)
#아니면
else:
  print(dp[k])