n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

ans = 999999999  #비용 최댓값

#dfs 시작,현재,방문한 도시 수,비용 합
def f(start, cur, cnt, cost_sum):
    #모든 도시 방문시
    if cnt == n:
        #w[cur][start]가 0이 아니라면
        if w[cur][start]:
            global ans          #가져옴
          #출발지로 가는 비용 추가,최소 비용 저장
            ans = min(ans, cost_sum + w[cur][start]) 
            return
    visit[cur] = 1  #도시 방문
    for i in range(n):  #반복문@
      #w[cur][i]가 0이 아니고 i 노드를 방문하지 않았다면
        if w[cur][i] and not visit[i]:
          #재귀함수 start 유지,i 변화,cnt 1 증가 ,비용증가
            f(start, i, cnt + 1, cost_sum + w[cur][i])
    #cur방문기록을 지움,방문 기록 지움 !! 중요@
    visit[cur] = 0  
    return

#도시 방문할 때마다 cnt 증가,비용증가-함수마다 정해진 cnt,cost가 있어
#이어할 수 있다

visit = [0] * n
#도시 수만큼 반복하며 함수 실행
for i in range(n):
    f(i, i, 1, 0)

print(ans)