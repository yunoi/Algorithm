# 챕터 10 (계속)

# 위상 정렬
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘.
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

# ex. 선수과목을 고려한 학습 순서 설정
# 자료구조 과목을 수강한 뒤에 알고리즘을 수강할 것을 권장하는 경우
# 자료구조와 알고리즘을 각가의 노드로 표현, 자료구조에서 알고리즘으로 이어질 수 있도록 방향성을 갖는 간선을 그릴 수 있다.
# 즉 그래프상에서 선후관계가 있다면 위상정렬을 수행하여 모든 선후관계를 지키는 전체 순서를 계산할 수 있다.

# 진입차수(indegree)
# 특정한 노드로 들어오는 간선의 개수

from collections import deque

print('노드 개수 및 간선 개수 입력')
node, edge = map(int, input().split())
indegree = [0] * (node+1) # 진입 차수 초기화
graph = [[] for i in range(node+1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화

print('방향 그래프의 모든 간선 정보 입력')
for _ in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b) # 정점 a에서 b로 이동 가능
  # 진입차수 1 증가
  indegree[b] += 1
  
# 위상 정렬 함수
def topology_sort():
  result = [] # 수행 결과 리스트
  q = deque() 
  
  # 처음 시작 시 진입차수 0인 노드 큐에 삽입
  for i in range(1, node+1):
    if indegree[i] == 0:
      q.append(i)
  
  # 큐가 빌 떄까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  print('위상 정렬 수행 결과 출력')      
  for i in result:
    print(i, end=' ')
    
topology_sort()