n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
arr = []

def cur(start):
    if len(arr) == m:
        print(*arr)
        return
    
    prev = 0
    for i in range(start,n):
        if prev !=  data[i]:
            arr.append(data[i])
            prev = data[i]
            cur(i+1)
            arr.pop()

cur(0)