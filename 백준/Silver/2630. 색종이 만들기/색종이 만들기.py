N = int(input())

white_count = 0
blue_count = 0

def divide(arr,n):
    global white_count
    global blue_count
    if n == 1:
        if arr[0][0] == 0:
            white_count += 1
        else:
            blue_count += 1
        return
    
    color  = color_check(arr,n)
    if color == 1:
        blue_count += 1
        return
    elif color == 0:
        white_count += 1
        return
   
    div1 = []
    div2 = []
    div3 = []
    div4 = []
    for i in range(n//2):
        div1.append(arr[i][:n//2])
        div2.append(arr[i][n//2:])
        div3.append(arr[n//2 + i][:n//2])
        div4.append(arr[n//2 + i][n//2:])
    
    divide(div1,n//2)
    divide(div2,n//2)
    divide(div3,n//2)
    divide(div4,n//2)


def color_check(arr,n):
    total = 0
    for i in range(n):
        total += sum(arr[i])
    if total == n * n:
        return 1
    if total == 0:
        return 0
    else:
        return 2
            
        
arr = [list(map(int,input().split())) for _ in range(N)]
divide(arr,N)
print(white_count)
print(blue_count)