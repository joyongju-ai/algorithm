#gpt 코드
from collections import deque

# 톱니바퀴 입력 (각 줄을 deque로 변환)
gears = []
for _ in range(4):
    gears.append(deque(input().strip()))

k = int(input())

# 회전 함수
def rotate(gear, direction):
    if direction == 1:        # 시계 방향
        gear.appendleft(gear.pop())
    elif direction == -1:     # 반시계 방향
        gear.append(gear.popleft())

for _ in range(k):
    idx, direction = map(int, input().split())
    idx -= 1  # 0-index로 변환

    rotate_dir = [0] * 4
    rotate_dir[idx] = direction

    # 왼쪽 방향 전파
    for i in range(idx - 1, -1, -1):
        # i(왼쪽)의 오른쪽(2) vs i+1(오른쪽)의 왼쪽(6)
        if gears[i][2] != gears[i+1][6]:
            rotate_dir[i] = -rotate_dir[i+1]
        else:
            break

    # 오른쪽 방향 전파
    for i in range(idx + 1, 4):
        # i(오른쪽)의 왼쪽(6) vs i-1(왼쪽)의 오른쪽(2)
        if gears[i][6] != gears[i-1][2]:
            rotate_dir[i] = -rotate_dir[i-1]
        else:
            break

    # 실제 회전 수행
    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(gears[i], rotate_dir[i])

# 점수 계산
score = 0
for i in range(4):
    if gears[i][0] == '1':
        score += (1 << i)

print(score)
