# 챕터 10 그래프이론 실전문제 3

# 커리큘럼

# 입력
# 듣고자하는 강의의 수 n 
# 그 다음 n 줄에 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호 자연수로 입력
# 강의 번호는 1~n. 각 줄은 -1로 끝남.

# 출력
# n 개의 강의에 대해 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력

from collections import deque
import copy

# 강의 개수 입력
n = int(input())

indegree = [0] * (n + 1)
graph = [[] for i in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
  data = list(map(int, input().split()))
  time[i] = data[0] # 첫 번째 수는 시간 정보
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(i)
    
# 위상 정렬 함수
def topology_sort():
  result = copy.deepcopy(time)
  q = deque()
  
  # 처음 시작시 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
  
  # 큐가 빌 때까지 반복
  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      
      if indegree[i] == 0:
        q.append(i)
        
  for i in range(1, n+1):
    print(result[i])
    
topology_sort()