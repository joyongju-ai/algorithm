import sys
input = sys.stdin.readline

n = list(input().rstrip())
data = list(map(int,n))

num =[[0]for i in range(10)]
for i in data:
    num[i][0] +=1
result = 0
for i in range(len(num)):
    if i == 6 or i == 9:
        set69 =(num[6][0] + num[9][0])//2 + (num[6][0] + num[9][0])%2
        result = max(result, set69)
    else:    
        result = max(num[i][0],result)

print(result)
    