N,r,c = map(int,input().split())
N = 2**N

def z(n,r,c):
    if n == 1:
        return 0
    
    half = n//2
    if r < half and c < half:
        return z(half,r,c) 
    elif r < half and c >= half:
        return half * half + z(half,r,c - half)
    elif r >= half and c < half:
        return 2* half * half + z(half,r - half,c)
    elif r >= half and c >= half:
        return 3 * half * half + z(half,r - half,c - half)
    
answer = z(N,r,c)
print(answer)