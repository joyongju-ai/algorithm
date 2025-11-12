l,c = map(int,input().split())
data = list(input().split())
data.sort()

aeious = []
others = []

password= []

for i in range(len(data)):
    if data[i] in ['a','e','i','o','u']:
        aeious.append(data[i])
    else:
        others.append(data[i])

def cur(start,aeiou,others):
    if len(password) == l:
        if aeiou >=1 and others >=2:
            print("".join(password))
        return
    
    for i in range(start,len(data)):
        password.append(data[i])
        if data[i] in aeious:
            cur(i+1,aeiou+1,others)
        else:
            cur(i+1,aeiou,others+1)
        password.pop()

cur(0,0,0)