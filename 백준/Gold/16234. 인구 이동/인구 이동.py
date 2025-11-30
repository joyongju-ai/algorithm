from collections import deque

n,L,R = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(n)]

days = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while True:
    visited = [[0]*n for _ in range(n)] # 날 바뀔 때마다 다시 연합 형성해야하므로 초기화
    num = 0
    flag = 0    # 연합형성 flag, 한 번이라도 형성하면 1
    arrs = []
    #bfs를 통해 조건에 맞게 flood fill로 연합 형성
    q = deque()
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                # 각 연합 구분 위해 visited를 연합 별로 num으로 써서 구분
                num += 1
                visited[r][c] = num
                q.append((r,c))
                arr = [(r,c)]
                while q:
                    x,y = q.popleft()
                    
                    for i in range(4):
                        nx,ny = x + dx[i], y + dy[i]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        # 인구 차가 L이상 R이하이고 미방문이면 
                        if not visited[nx][ny] and L <= (abs(A[nx][ny] - A[x][y])) <= R:
                            visited[nx][ny] = num
                            q.append((nx,ny))
                            arr.append((nx,ny))
                            flag = 1
                arrs.append(arr)
    # 한 번도 연합 형성 안 했으면
    if flag == 0: 
        break            
    
    days += 1   #일 수 추가
    
    # 인구이동 실행  
    for i in range(len(arrs)):     # 연합 번호별 진행 
        total = 0           # 총합
        for x,y in arrs[i]:
            total += A[x][y]
        
        for x,y in arrs[i]:
            A[x][y] = total//(len(arrs[i]))
            

print(days)      