#왜인지 피보나치 수열이 생각나서 재귀함수로 풀었다
#수열의 메커니즘이 같다면 재귀함수로 해결할 수 있다는 것을 알았다
#number_maker,인덱스로 문제 해결

#중요 
#number_maker의 아이디어
#인덱스 아이디어


#내 풀이
#입력부
first,p=map(int,input().split())


d_nums=[first]  #수열 d

#각 자리 숫자 만드는 함수,0은 추출하지 않음
def number_maker(pre_d,numbers):
  div=10**(len(str(pre_d))-1)  #10의 pre_d 자릿 수 제곱 
  a=pre_d//(div)           
  numbers.append(a)           #나눈 몫을 추가
  b=pre_d%div                 #나눈 나머지

  #나눈 나머지가 0이면 유효한 숫자가 없는 것이므로 종료
  if b==0:
    return 
  #아니면 나머지로 다시 숫자를 만든다
  else:
    number_maker(b,numbers)

    
#다음 수열 형성하고 수열 d에 추가하는 함수
def next_d(pre_d):
  #자리 수 별로 숫자를 나누어 다음 수열 만들기
  numbers=[]    #각 자리 숫자 받는 배열 초기화
  result=0      #다음 항 결과 값
  number_maker(pre_d,numbers)  
  #숫자 배열에서 하나씩 꺼내 계산
  for i in numbers:
    result+=(i**p)

  #만약 다음 수열이 수열 d에 없다면
  if result not in d_nums:
    #수열 d에 추가
    d_nums.append(result)
    #다음 수열 호출
    return next_d(result)
  #만약 다음 수열이 수열 d에 있다면,즉 이미 나왔던 적 있는 수라면
  else:
    #해당 수의 인덱스를 d에서 찾는다
    index=d_nums.index(result)
    return index  #인덱스 반환


index=next_d(first)        #index 받기
answer=len(d_nums[0:index])  #인덱스 이전까지만 길이 재기

print(answer)  #결과 출력