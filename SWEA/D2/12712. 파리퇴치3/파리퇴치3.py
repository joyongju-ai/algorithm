T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    
    array = [list(map(int,input().split())) for i in range(n)]
   
    dx = [0,1,0,-1,-1,1,-1,1]
    dy = [1,0,-1,0,-1,-1,1,1]
    
    def cross(x,y,m):
        crosskill = array[x][y]
        for k in range(4):
            a = 0
            
            while (a < m -1):
                nx , ny = x + dx[k]*(a+1), y + dy[k]*(a+1)
                if nx <0 or nx >=n or ny <0 or ny >= n:
                    break
                crosskill += array[nx][ny]
                a += 1
        return crosskill
        
    def xcross(x,y,m):
        xkill = array[x][y]
        for k in range(4):
            a = 0
            while (a < m - 1 ):
                nx , ny = x + dx[k+4]*(a+1), y + dy[k+4]*(a+1)
                if nx <0 or nx >=n or ny <0 or ny >= n:
                    break
                xkill += array[nx][ny]
                a += 1
        return xkill
        
    max_kill = 0
    for i in range(n):
        for j in range(n):
            kill = array[i][j]
            cross_kill = cross(i,j,m)
            x_kill = xcross(i,j,m)
            result = max(cross_kill,x_kill) 
            max_kill = max(max_kill,result)
            #print(i,j,"k",x_kill,cross_kill,max_kill)
            
    
    print(f"#{test_case}", max_kill)
                
    
