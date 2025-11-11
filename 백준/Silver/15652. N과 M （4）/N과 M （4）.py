n,m = map(int,input().split())

arr = []

def cur(start):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start,n+1):
        arr.append(i)
        cur(i)
        arr.pop()

cur(1)