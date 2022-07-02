# 챕터 9 최단 경로 (계속)
# 속도개선 다익스트라 분석

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n,m = map(int, input().split()) # 6 11
# 시작 노드 번호 입력
start = int(input()) # 1
# 노드 정보 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)
print(distance) # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
# 모든 간선 정보 입력
# 1 2 2 
# 1 3 5 
# 1 4 1
# 2 3 3 
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
for _ in range(m): # 11
  a,b,c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c
  graph[a].append((b,c))

print(graph) # [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

temp_q = []
heapq.heappush(temp_q, (0, start))
distance[start] = 0
print(temp_q) # [(0, 1)]
print(distance) # [1000000000, 0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]

def dijkstra(start): # 1
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start)) 
  distance[start] = 0 # distance[1] = 0
  while q: # 큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    print('q', q)
    print('dist, now: ', dist, now) # 최단거리, 현재 인덱스
    # 현재 노드가 이미 처리된 적 있는 노드라면 무시
    if distance[now] < dist: # 현재 인덱스의 최단 거리 테이블 값이 최단거리보다 작다
      continue # 스킵
    # 현재 노드와 연결된 다른 인접한 노드들 확인
    for i in graph[now]: # graph[1] == [(2, 2), (3, 5), (4, 1)]
      cost = dist + i[1] # (2,2)[1] == 2, (3,5)[1] == 5, (4,1)[1] == 1
      print('i', i) # (2,2), (3,5), (4,1)
      print('graph[now]', graph[now]) # [(2, 2), (3, 5), (4, 1)] 
      print('i[1]', i[1]) # (2, 2)일 때 2, (3, 5)일 때 5, (4,1)일 떄 1
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]: # 2 < distance[2] == INF, 5 < INF, 1 < distance[1] == 0(False)
        distance[i[0]] = cost # distance[2] = 2, distrance[3] = 5
        heapq.heappush(q, (cost, i[0])) # q[(2, 2), (5, 3)]

# 다익스트라 알고리즘 콜
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])
    
# 실전문제: 미래도시
# 1~n번 회사
# 특정 회사끼리 서로 도로를 통해 연결
