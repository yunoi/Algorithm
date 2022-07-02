# 챕터 9 최단 경로
# 1. 가장 빠른 길 찾기
# 가장 빠르게 도달하는 방법. 일명 '길 찾기' 문제.
# ex. 한 지점에서 다른 특정 지점까지의 최단 경로를 구하기, 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하기 등.
# 보통 그래프를 이용해 표현. 각 지점은 노드로 표현되고, 지점 간 연결된 도로는 간선으로 표현.
# 다익스트라 최단 경로 알고리즘, 플로이드 워셜, 벨만 포드 알고리즘.
# 그리디 알고리즘 및 다이나믹 프로그래밍 알고리즘의 한 유형.

# 다익스트라 최단 경로 알고리즘
# 여러 개의 노드가 있을 때, 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘.
# 음의 간선이 없을 때 정상 동작.
# 음의 간선: 0보다 작은 값을 가지는 간선.
# 현실에서는 GPS 소프트웨어의 기본 알고리즘으로 채택되는 경우가 많음.
# 원리
# 1. 출발 노드 설정.
# 2. 최단 거리 테이블 초기화.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신.
# 5. 위 과정에서 3, 4번을 반복.

# 최단 경로를 구하는 과정에서 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 갱신
# (1차원 리스트 == 최단 거리 테이블)
# 매번 현재 처리하고 있는 노드를 기준으로 주변 간선 확인.
# 구현 방법 2가지
# 1. 구현하기 쉽지만 느리게 동작하는 코드
# 2. 구현하기 조금 더 까다롭지만 빠르게 동작하는 코드

# 무한으로 초기화
# 999999999 (약 10억)
# 자릿수를 헷갈리지 않게 987654321로 설정하기도 함.
# 지수표기법으로 1e9를 사용
# 파이썬에서 기본으로 1e9를 실수 자료형으로 처리하므로 모든 간선이 정수형으로 표현되는 문제에서 int(1e9)로 초기화

# 예시
# 0. 먼저 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택. 출발 노드에서 출발 노드로의 거리는 0으로 보기 때문에 처음에는 출발 노드가 선택됨.
# 노드번호 1   2    3    4    5    6
#     거리 0 무한 무한 무한 무한 무한
# 1. 1번 노드를 거쳐 다른 노드로 가는 비용을 계산.
#    즉 1번 노드와 연결된 모든 간선을 하나씩 확인.
#    2, 3, 4번으로 가는 최소 비용 == 2, 5, 1
#    무한으로 설정된 값을 위의 값으로 갱신
# 처리 결과 
# 노드번호 1   2    3    4    5    6
#     거리 0   2    5    1  무한 무한
# 2. 이후 모든 단계에서도 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택.
#    따라서 4번 노드 선택.
#    이어서 4번 노드를 거쳐서 갈 수 있는 노드 확인 == 3, 5
#    최단 거리 == 1+3, 1+1
#    기존 리스트에 담긴 값보다 작으므로 리스트 갱신
# 처리 결과
# 노드번호 1   2    3    4    5    6
#     거리 0   2    4    1    2  무한
# 3. 2번 노드 선택
#    2번 노드를 거쳐서 도달할 수 있는 노드 중 거리가 더 짧은 경우가 존재하는지 확인
#    있으면 계산하여 갱신, 없으면 유지
# 4. 위와 같은 방식으로 반복.

# 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾을 수 있음.

# 간단한 다익스트라 알고리즘 구현
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 선언
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 선언
visited = [False] * (n+1)
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
  a,b,c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_shortest_node():
  min_value = INF
  index = 0 # 가장 최단거리가 짧은 노드 (인덱스)
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_shortest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한(INFINITYU) 출력
  if distance[i] == INF:
    print('INFINITY')
  # 도달할 수 있는 경우 거리 출력
  else:
    print(distance[i])