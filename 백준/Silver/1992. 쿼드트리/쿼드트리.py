N = int(input())
arr = [list(input()) for _ in range(N)]

quad =""
def divide(x,y,n):
    global quad
    same = check(x,y,n)
    if same == "1":
        quad += "1"
        return
    elif same == "0":
        quad += "0"
        return
    quad += "("
    half = n//2
    for i in range(2):
        for j in range(2):
            divide(x+i*half,y+j*half,half)
    quad += ")"

def check(x,y,n):
    base = arr[x][y]
    
    for i in range(n):
        for j in range(n):
            if base != arr[x+i][y+j]:
                return 2
    return base

divide(0,0,N)
print(quad)