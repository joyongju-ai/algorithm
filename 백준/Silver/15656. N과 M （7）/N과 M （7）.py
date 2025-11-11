n,m = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
arr = []

def cur():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(len(data)):
        arr.append(data[i])
        cur()
        arr.pop()

cur()