# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

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
