a,b,c = map(int,input().split())

def pow(a,b,c):
    if b == 1:
        return a % c
    val = pow(a,b//2,c)
    val = (val*val)%c

    if b %2 == 0:
        return val
    else:
        return (val*a)%c

result = pow(a,b,c)
print(result)