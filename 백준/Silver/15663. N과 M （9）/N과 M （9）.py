n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
arr=[]
visited = [0]*(len(data))

def cur():
    if len(arr)==m:
        print(*arr)
        return
    prev = 0
    for i in range(len(data)):
        if not visited[i] and prev != data[i]:
            visited[i] = 1
            arr.append(data[i])
            prev = data[i]
            cur()
            visited[i] = 0
            arr.pop()
cur()