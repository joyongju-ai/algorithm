import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int,input().rstrip().split()))
x = int(input().rstrip())


dp = [0]*(2000001)

data.sort()
count = 0
for i in range(n):
    dp[data[i]] += 1
    if data[i] != x -data[i] and dp[x - data[i]] == 1:
        count +=1

print(count)