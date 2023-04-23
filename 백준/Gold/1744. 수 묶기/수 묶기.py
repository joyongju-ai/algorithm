n=int(input())

num=[int(input()) for i in range(n)]

#1은 곱하면 무조건 합이 작아지므로 더해준 뒤 모두 제거한다
ones=num.count(1)
result=1*ones              #결과 변수
for i in range(ones):
  num.remove(1)

#남은 것들을 양수,음수와 0으로 나누어 저장한다
#양수의 경우 0과 곱하면 무조건 수가 작아지므로 0은 음수와 같은 리스트로 저장한다
plus_num=[]
minus_num=[]
for i in num:
  if i>0:
    plus_num.append(i)
  else:
    minus_num.append(i)

#양수는 내림차순으로,음수와 0은 오름차순으로 정렬한다
plus_num.sort()
plus_num.reverse()
minus_num.sort()

#양수를 앞에서부터 차례로 2개씩 묶어준다
for i in range(0,len(plus_num)-1,2):
  result+=plus_num[i]*plus_num[i+1]
#만약 길이가 홀수면 남은 하나는 묶을 수 없으므로 더해줘야 한다
if len(plus_num)%2==1:
  result+=plus_num[-1]
  
#음수와 0을 앞에서부터 차례로 2개씩 묶어준다
for i in range(0,len(minus_num)-1,2):
  result+=minus_num[i]*minus_num[i+1]
#만약 길이가 홀수면 남은 하나는 묶을 수 없으므로 더해줘야 한다
if len(minus_num)%2==1:
  result+=minus_num[-1]
  
print(result)