n=int(input())

#입력 받는 동시에 난이도 내림차순 정렬(역순 정렬)
data=[int(input()) for _ in range(n)][::-1]

score=data[0]        #기준 점수
count=0              #줄인 횟수

for i in data[1:]:
  #기준 점수보다 높거나 같다면
  if i>=score:
    #기준 점수 -1과의 차만큼 줄여준다,count증가
    count+=i-(score-1)
    #기준 점수-1
    score-=1
  #기준 점수보다 작다면
  else:
    #기준점수는 그 점수로 한다
    score=i


print(count)