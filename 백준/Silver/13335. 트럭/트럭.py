n,w,l = map(int,input().split())

truck_weight = list(map(int,input().split()))
count = 0


#다리 이동 총괄
def move():
    global count
    bridge = [0] * w  # 다리 길이만큼 부여
    i = 0
    while True:
        if i == n and sum(bridge) == 0:
            break
        bridge2 = [x for x in bridge]
        if i < n and sum(bridge) + truck_weight[i] <= l:
            bridge2 = step(bridge2)
            bridge2[-1] = truck_weight[i]
            count += 1
            i += 1
        elif i < n and sum(bridge) + truck_weight[i] > l:
            for j in range(w):
                if bridge[j] > 0:
                    idx = j
                    break
            for _ in range(idx+1):
                bridge2 = step(bridge2)
                count += 1
            if i < n and sum(bridge2) + truck_weight[i] <= l:
                bridge2[-1] = truck_weight[i]
                i += 1
        elif i == n:
            bridge2 = step(bridge2)
            count += 1
        bridge = [y for y in bridge2]
        #print(bridge,count)


# 다리 위의 차가 1번 이동하는 함수
def step(bridge):
    changed_bridge = [0]*w
    for i in range(w):
        if bridge[i] == 0:
            continue
        if i == 0:
            continue
        elif i > 0:
            changed_bridge[i-1] = bridge[i]
    #print(changed_bridge)
    return changed_bridge


move()
print(count)