#그리디 
#아이디어
#앞으로 나오지 않는 기구를 뻬고 새 기구를 넣는다
#그런 기구가 없다면 앞으로 가장 늦게 나오는 기구를 빼고 새 기구를 넣는다

import sys

input=sys.stdin.readline

n,k=map(int,input().split())

q=list(map(int,input().split()))

codes=[]           #코드에 넣은 기구 리스트
count=0            #교체 횟수

#q전체를 살펴보며
for i in range(len(q)):
  #codes가 다 차지 않았다면
  if len(codes)<n:
    #q[i]가 codes에 없다면 추가
    if q[i] not in codes:
      codes.append(q[i])
  else:  
    #코드에 이미 있는 기구이면 continue
    if q[i] in codes:
      continue
    #아니면 늦게 나오는 기구 빼고 새 기구 넣기
    else:
      idx=-2           #삭제할 항 인덱스   
      count+=1          #교체 횟수 증가
      #codes의 각 항을 살펴보며
      for j in codes:
        #만약 이후의 q에 없다면 해당 항 삭제,새 기구 추가
        if j not in q[i+1:]:
          idx=-1          #-1로 만들어서 구별
          codes.remove(j)    
          codes.append(q[i])
          break 
        #있다면 가장 늦게 나오는 항의 인덱스 체크
        else:
          idx=max(idx,q[i+1:].index(j))
  
      #가장 늦게 나오는 항 삭제 후 새 기구 추가
      if idx!=-1:
        codes.remove(q[i+1:][idx])
        codes.append(q[i])
  
print(count)