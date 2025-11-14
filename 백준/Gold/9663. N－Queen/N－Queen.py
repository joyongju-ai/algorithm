def cur(depth):
    global count
    if depth == n:
        count += 1
        return
    
    for i in range(n):
        if column_visit[i] or right_slash[depth-i +(n-1)] or left_slash[depth+i]:
            continue
        else:
            column_visit[i] = 1
            right_slash[depth-i +(n-1)] = 1
            left_slash[depth+i] = 1
            cur(depth+1)
            column_visit[i] = 0
            right_slash[depth-i +(n-1)] = 0
            left_slash[depth+i] = 0

n = int(input())

column_visit = [0]*40
right_slash = [0]*40
left_slash= [0]*40

count = 0

cur(0)
print(count)