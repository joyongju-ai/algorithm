from itertools import combinations

n,m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]

houses = []
chickens = []
for row in range(n):
    for col in range(n):
        if space[row][col] == 1:
            houses.append((row,col))
        if space[row][col] == 2:
            chickens.append((row,col))

min_dist = int(1e9)
for comb in combinations(chickens,m):
    total_dist = 0
    for x1,y1 in houses:
        chicken_dist = int(1e9)
        for x2,y2 in comb:
            chicken_dist = min(chicken_dist, (abs(x1-x2) + abs(y1 - y2)))
        total_dist += chicken_dist
    min_dist = min(min_dist, total_dist)

print(min_dist)
