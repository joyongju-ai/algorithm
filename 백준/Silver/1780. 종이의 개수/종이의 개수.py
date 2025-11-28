N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

minus = 0
zero = 0
one = 0

def divide(x,y,n):
    global minus,zero,one
    same = check(x,y,n)
    if same == -1:
        minus += 1
        return
    elif same == 0:
        zero += 1
        return
    elif same == 1:
        one += 1
        return
    tri = n//3
    for i in range(3):
        for j in range(3):
            divide(x+i*tri,y+j*tri,tri)

def check(x,y,n):
    base = arr[x][y]
    
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != base:
                return 2
    return base 


divide(0,0,N)
print(minus)
print(zero)
print(one)