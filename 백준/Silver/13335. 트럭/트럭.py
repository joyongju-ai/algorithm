from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 길이가 w인 다리를 큐로 모델링한 것
# 큐의 왼쪽이 다리의 입구, 오른쪽이 다리의 끝
# 0은 빈 자리 → 트럭이 없는 공간을 의미
bridge = deque([0]*w)  # 큐 이용
time = 0            # 다리 건너는 시간
weight = 0          # 다리 위 트럭들의 무게 합

for t in trucks:            #트럭 하나씩 처리
    # 트럭 넣을 때까지 반복
    while True:
        time += 1
        weight -= bridge.popleft()  # 맨 앞 트럭 나감, 무게 감소 

        # 새 트럭이 올라갈 수 있으면 올리고 break
        if weight + t <= L:         
            bridge.append(t)        # 트럭을 다리에 올리기
            weight += t             # 무게 추가
            break
        else:
            bridge.append(0)  # 트럭이 못 올라오면 빈 칸 밀기

time += w # 마지막으로 다리에 올라간 트럭을 건너게 하기 위해
print(time)
