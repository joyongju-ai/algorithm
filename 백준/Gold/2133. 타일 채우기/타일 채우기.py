#아이디어 
#3*n의 타일에 주어진 블록 ㅣ,ㅡ로 만들 수 있는 조합을 생각해봤다
#3*1,3*3은 채울 수 없고 3*2,3*4,3*6까지가 최대
#i번째를 구할 때 i-2에 3*2타일을 붙이는 경우 3
#i-n(n은 4,...,i-2)에 타일을 붙이는 경우는 각각 2이다
#붙이지 않고 만들 수 있는 경우도 2가지 있다

n=int(input())
#dp테이블 초기화
dp=[0]*31
dp[2]=3            #초깃값

for i in range(4,n+1,2):
  #i-2에 3*2 붙이는 경우 3
  dp[i]=dp[i-2]*3
  #i-n에 3*n 타일 붙이는 경우 각각 3
  for j in range(4,i,2):
    dp[i]+=dp[i-j]*2
  #붙이지 않고 0에서 만드는 경우 2
  dp[i]+=2

print(dp[n])