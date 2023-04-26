#아이디어
#입력받은 날짜는 월*100+일로 변환한다.-다른 문제에서도 쓰이는 스킬이니 숙지
#기준 시간 end_time보다 이전에 피면서 가장 뒤에 지는 꽃을 계속해서 추가한다
#end는 301에서 시작해 지속적으로 갱신한다

from collections import deque
n=int(input())

#꽃의 피는 시기, 지는 시기를 월*100+일로 만든 후 저장
flower=[]
for i in range(n):
  a,b,c,d=map(int,input().split())
  start=100*a+b
  end=100*c+d
  flower.append([start,end])

#피는 날,지는 날 순으로 오름차순
flower.sort()

end=301    #지는 날
temp=0     #임시 end
count=0    #꽃 종류

q=deque(flower)    
#큐가 빌 때까지
while q:
  #만약 지는 시간이 12월 1일이거나 
  #피는 시기가 지는 시기보다 뒤이면 종료
  if end>=1201 or end<q[0][0]:
    break
  count+=1      #꽃 종류 증가
  while q:
    #지는 시간 이전에 꽃이 피는 경우
    if end>=q[0][0]:
      x,y=q.popleft()    #각 꽃의 시작,끝 뽑기
      temp=max(temp,y)   #지는 시간이 가장 늦은 것 temp에 저장
    #아닌 경우 탈출
    else:
      break
  #end 갱신
  end=temp


if end>=1201:
  print(count)
else:
  print(0)