n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
arr  = []

def cur():
    if len(arr) == m:
        print(*arr)
        return
    prev = 0
    for i in range(len(data)):
        if prev != data[i]:
            arr.append(data[i])
            prev = data[i]
            cur()
            arr.pop()

cur()