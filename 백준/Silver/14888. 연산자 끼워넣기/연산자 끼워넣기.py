from itertools import permutations

n=int(input())
numbers=list(map(int,input().split()))
calculate=list(map(int,input().split()))

calculate_array=[]
for i in range(len(calculate)):
  if calculate[i]==0:
    pass
  else:
    for j in range(calculate[i]):
      if i==0:
        calculate_array.append("+")
      elif i==1:
        calculate_array.append("-")
      elif i==2:
        calculate_array.append("*")
      elif i==3:
        calculate_array.append("//")

calculate_cases=permutations(calculate_array,n-1)
result=numbers[0]
max_result=-(int(1e9))
min_result=int(1e9)
for case in calculate_cases:
  for i in range(len(case)):
    if case[i]=="+":
      result+=numbers[i+1]
    if case[i]=="-":
       result-=numbers[i+1]
    if case[i]=="*":
       result*=numbers[i+1]
    if case[i]=="//":
      if result>0:
        result=result//numbers[i+1]
      elif result<0:
        result=-((-result)//numbers[i+1]) 
  max_result=max(max_result,result)
  min_result=min(min_result,result)
  result=numbers[0]
  
print(max_result)
print(min_result)