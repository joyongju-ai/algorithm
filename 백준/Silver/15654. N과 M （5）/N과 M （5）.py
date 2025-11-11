n,m = map(int,input().split())

data = list(map(int,input().split()))
data.sort()

visited= [0]*(len(data))

arr = []

def cur():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(len(data)):
        if not visited[i]:
            arr.append(data[i])
            visited[i] = 1
            cur()
            arr.pop()
            visited[i] = 0

cur()