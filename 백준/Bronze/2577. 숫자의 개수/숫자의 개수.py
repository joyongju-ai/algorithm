import sys
input = sys.stdin.readline

result = 1
for i in range(3):
    n = int(input().rstrip())
    result *= n

nums = list(str(result))
dp = [0]*10

for i in range(len(nums)):
    dp[int(nums[i])] += 1

for i in range(len(dp)):
    print(dp[i])
