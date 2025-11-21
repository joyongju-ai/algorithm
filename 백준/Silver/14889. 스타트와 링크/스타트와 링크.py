n = int(input())
data = [x for x in range(1,n+1)]
teams = []
arr = []
s = [list(map(int,input().split())) for i in range(n)]

total = 0
for i in range(n):
    for j in range(n):
        total += s[i][j]


def cur(start):
    if len(arr) == n//2:
        #print(arr)
        arr_copy = [x for x in arr]
        teams.append(arr_copy)
        return

    for i in range(start,n):
        arr.append(data[i])
        cur(i+1)
        arr.pop()


cur(0)
gap = 1e9
#print(teams)
for team in teams:
    team_total = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if team[i] != team[j]:
                team_total += s[team[i]-1][team[j]-1]
    #print(team_total)

    others = []
    for x in data:
        if x not in team:
            others.append(x)
    others_total = 0
    for i in range(len(others)):
        for j in range(len(others)):
            if others[i] != others[j]:
                others_total += s[others[i]-1][others[j]-1]
    #print(others_total)
    gap = min(gap, abs(team_total - others_total))
    #print(gap)

print(gap)