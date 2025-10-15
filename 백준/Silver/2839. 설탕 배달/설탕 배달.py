n = int(input())

def sugar(n):
    numlist = [[10000] for i in range(5001)]
    numlist[0][0] = 0
    numlist[3][0] = 1
    numlist[5][0] = 1
    for i in range(6,n+1):
        numlist[i][0] = 1 + min(numlist[i-3][0],numlist[i-5][0])
    if numlist[n][0] < 10000:
        return numlist[n][0]
    else:
        return -1
        
result = sugar(n)
print(result)