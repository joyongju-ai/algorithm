n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

arr = []
def cur(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start,len(data)):
        arr.append(data[i])
        cur(i+1)
        arr.pop()

cur(0)