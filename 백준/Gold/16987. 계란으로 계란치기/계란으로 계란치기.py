n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
count = 0

life = [eggs[i][0] for i in range(n)]

def cur(depth,arr):
    global count 
    if  depth == n:
        count = max(count,arr.count(0))
        return 
    
    temp = [x for x in arr]
    flag = False
    for i in range(n):
        if i != depth and temp[depth] and temp[i]:
            flag = True
            arr = [x for x in temp]
            if temp[depth] <= eggs[i][1]:
                arr[depth] = 0
            else:
                arr[depth] = temp[depth] - eggs[i][1]
            if temp[i] <= eggs[depth][1]:
                arr[i] = 0
            else:
                arr[i] = temp[i] -eggs[depth][1]
            cur(depth+1,arr)
    if flag == False:
        cur(depth+1,temp)
        
cur(0,[eggs[i][0] for i in range(n)])
print(count)