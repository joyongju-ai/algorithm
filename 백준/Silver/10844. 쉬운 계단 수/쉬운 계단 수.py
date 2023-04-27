#dp
#모든 경우를 구하려면 엄청난 수의 연산을 해야함
#무슨 방법이 있을 것이다->dp or 그리디 중 생각

#아이디어
#자릿수 늘릴 때마다 뒤에 숫자를 붙인다
#붙이는 수에 따른 계단 수를 dp에 저장한다
#temp_dp[j]=dp[j-1]+dp[j+1]->temp 안 쓰면 원본 훼손이 돼서
#마지막에 dp의 합이 자릿수에 따른 계단 수이다


n=int(input())

#dp테이블 초기화
dp=[1]*10      #뒤에 붙이는 수에 따른 dp
dp[0]=0

#2부터 n자릿수까지 차례로 올려가며
for i in range(2,n+1):
  temp_dp=[0]*10       #원본훼손 막기 위한 임시 테이블
  #dp 테이블 살펴보기,붙이는 수 j
  for j in range(10):
    #마지막 수가 0인 경우
    if j==0:
      temp_dp[j]=dp[j+1]
    #마지막 수가 9인 경우
    elif j==9:
      temp_dp[j]=dp[j-1]
    else:
      temp_dp[j]=dp[j-1]+dp[j+1]
  dp=temp_dp[:]  #dp테이블 갱신


print(sum(dp)%1000000000)