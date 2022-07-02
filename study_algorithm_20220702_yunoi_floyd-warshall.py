# 챕터 9 최단 경로 (계속)
# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용
# 단계마다 거쳐 가는 노드를 기준으로 알고리즘 수행
# 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다는 점이 다익스트라 알고리즘과의 차이
# 다이나믹 프로그래밍

INF = int(1e9)

# 노드개수, 간선 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현) 만들고, 모든 값 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아 초기화
for _ in range(m):
  # a에서 b로 가는 비용은 c라고 설정
  a,b,c = map(int, input().split())
  graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print('INFINITY', end=" ")
    else:
      print(graph[a][b], end=" ")
  print()
  