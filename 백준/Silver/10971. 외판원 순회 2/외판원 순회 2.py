from itertools import permutations

n=int(input())

data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

cases=[]
for i in range(n):
  cases.append(i)
  
root_cases=permutations(cases,n)

result=0
answer=10000001
for root_case in root_cases:
  root_case=list(root_case)
  root_case.append(root_case[0])
  for i in range(len(root_case)-1):
    if data[root_case[i]][root_case[i+1]]!=0:
      result+=data[root_case[i]][root_case[i+1]]
    else:
      result=10000001
      break
  answer=min(answer,result)
  result=0
  
print(answer)