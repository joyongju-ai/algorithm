import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
v = int(input().rstrip())

dp = [0]*(201)

count = 0
for i in range(len(nums)):
    if nums[i] == v:
        count += 1

print(count)