import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

dp = [0] * (n+1)
flag = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    flag[i] = i -1
    if i%2 == 0:
        if dp[i] > dp[i//2]+1:
            flag[i] = i//2
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0:
        if dp[i] > dp[i//3]+1:
            flag[i] = i//3
        dp[i] = min(dp[i],dp[i//3]+1)
    
print(dp[n])
queue = deque([n])
while queue:
    num = queue.popleft()
    print(num, end = ' ')
    if num == 1:
        break
    queue.append(flag[num])