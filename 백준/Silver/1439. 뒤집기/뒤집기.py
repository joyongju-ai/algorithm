s=input()

#문자열 리스트로 넣기
array=[]
for i in s:
  array.append(int(i))
  
one=0          #연속된 1로 이루어진 그룹수
zero=0         #연속된 0으로 이루어진 그룹수
#리스트의 각 요소를 확인하며 그룹수를 센다
for i in range(len(array)-1):
  #현재 1이고 다음 수가 다르면 one 추가
  if array[i]==1 and array[i]!=array[i+1]:
    one=one+1
    #다음 수를 볼 수 없는 마지막 항은 이전 항과 달랐다면 반대쪽을 1증가
    #zero 그룹 수 세고 있었으면 one 증가하고,one 그룹 수 세고 있었으면       zero증가
  if array[i+1:].count(0)==len(array)-i-1:
    zero=zero+1
  #현재 0이고 다음 수가 다르면 zero 추가
  if array[i]==0 and array[i]!=array[i+1]:
    zero=zero+1
    #zero 그룹 수 세고 있었으면 one 증가하고,one 그룹 수 세고 있었으면       zero증가
  if array[i+1:].count(1)==len(array)-i-1:
     one=one+1
    
#둘 중 더 작은 그룹수를 출력한다
if zero<one:
  print(zero)
else:
  print(one)