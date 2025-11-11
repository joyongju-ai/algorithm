n,m = map(int,input().split())

arr= []

def cur():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        arr.append(i)
        cur()
        arr.pop()

cur()