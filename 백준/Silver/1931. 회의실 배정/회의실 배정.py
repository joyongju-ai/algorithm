n=int(input())

data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

data.sort(key=lambda x: (x[1],x[0]))

end=0
count=0
for i in data:
  if i[0]>=end:
    end=i[1]
    count+=1

print(count)