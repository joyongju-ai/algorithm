n,m = map(int,input().split())
array = []
visited = [0]*(n+1)

def cur(length):
    if length == m:
        print(*array)
        return
    for i in range(1,n+1):
        if not visited[i]:
            if not array or array[-1] < i:
                visited[i] = 1
                array.append(i)
                cur(length+1)
                visited[i] = 0
                array.pop()


cur(0)