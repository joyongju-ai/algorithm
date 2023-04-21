n=int(input())

data=[]
for i in range(n):
  data.append(int(input()))

#내림차순으로 나열
data.sort(key=lambda x: -x)
#로프 개수와 무게
weight=0
count=0
#들 수 있는 무게가 더 클 때만 무게 갱신 아닌 경우 바로 탈출
for i in data:
  count+=1
  if weight/count<=i:
    weight=i*count
  
print(weight)