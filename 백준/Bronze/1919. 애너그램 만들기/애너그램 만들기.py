import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list(input().rstrip())

dp1 = [0] * 26
dp2 = [0] * 26

for i in range(len(str1)):
    index1 = ord(str1[i])-ord('a')
    dp1[index1] += 1

for i in range(len(str2)):
    index2 = ord(str2[i])-ord('a')
    dp2[index2] += 1

count = 0
for i in range(len(dp1)):
    if dp1[i] == dp2[i]:
        count += dp1[i]*2
    else:
        count += min(dp1[i],dp2[i])*2
result = len(str1) + len(str2) - count

print(result)
    