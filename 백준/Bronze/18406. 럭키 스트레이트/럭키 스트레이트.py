n=input()

array=[]

for i in n:
  array.append(int(i))

mid=len(array)//2
#반으로 나누고 각자의 합 비교
if sum((array[:mid])) == sum(array[mid:]):
  print("LUCKY")
else:
  print("READY")