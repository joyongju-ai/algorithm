import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
v = int(input().rstrip())

dp = [0]*(201)

for i in range(len(nums)):
    dp[nums[i]+100] += 1
        
print(dp[v+100])