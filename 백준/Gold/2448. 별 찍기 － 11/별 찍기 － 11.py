N = int(input())

init = ["  *  "," * * ","*****"]

def cur(arr,n):
    if n == N:
        return arr
    tmp = []
    #print(arr)
    for i in range(n):
        tmp.append(" "*n +arr[i] + " "*n)
    for i in range(n):
        tmp.append(arr[i] + " " + arr[i])
    return cur(tmp,n*2)

answer = cur(init,3)

for line in answer:
    print(line)