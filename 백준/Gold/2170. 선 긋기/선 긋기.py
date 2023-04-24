#그리디
#시작과 끝 순으로 정렬 후 이어지는 길이를 각각 구해 더한다
import sys
input=sys.stdin.readline

n=int(input())

data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

#시작 순,종료 순으로 정렬
data.sort()

#start,end를 최솟값으로 초기화
start=data[0][0]
end=data[0][1]

result=0    #결과 길이 변수
for i in range(1,n):
  #시작이 end보다 이하라면 end를 최댓값으로 갱신
  if end>=data[i][0]:
    end=max(end,data[i][1])
  #아니라면 
  else:
    #그 때까지의 길이 결과에 더함
    result+=end-start
    #새로운 시작과 끝 
    start=data[i][0]
    end=data[i][1]

#위 반복문은 마지막 길이를 구할 수 없으므로 마지막 길이 더해준다
#새로운 시작과 끝이 나올 때만 길이를 더하기 때문
result+=end-start

print(result)