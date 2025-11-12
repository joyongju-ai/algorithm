while True:
    data = list(map(int,input().split()))
    if data[0] == 0:
        break
    k = data[0]
    num_set = data[1:]
    arr = []
    
    def cur(start):
        if len(arr) == 6:
            print(*arr)
            return
        
        for i in range(start,k):
            arr.append(num_set[i])
            cur(i+1)
            arr.pop()
    
    cur(0)
    print()