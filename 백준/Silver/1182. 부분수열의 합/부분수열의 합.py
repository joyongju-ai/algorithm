n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def dfs(idx, total):
    global count
    if idx == n:
        if total == s:
            count += 1
        return
    
    dfs(idx+1, total)          
    dfs(idx+1, total + arr[idx])  

dfs(0, 0)

# 공집합 제외
if s == 0:
    count -= 1

print(count)
