data=input()
numbers=[]
number=""
for i in range(len(data)):
  if data[i]=="-" or data[i]=="+":
    numbers.append(int(number))
    number=""
    if data[i]=="-":
      numbers.append(data[i])
  else:
    number=number+data[i]

numbers.append(int(number))

arr=[]
sum=0
for i in numbers:
  if i!="-":
    sum+=i
  else:
    arr.append(sum)
    sum=0
arr.append(sum)

ans=arr[0]
for i in arr[1:]:
  ans-=i

print(ans)