import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    temp = list(input().rstrip().split())
    str1 = list(temp[0])
    str2 = list(temp[1])
    str1.sort()
    str2.sort()
    if str1 == str2:
        print("Possible")
    else:
        print("Impossible")

        