# chapter 5. DFS/BFS
# 탐색 알고리즘

from collections import deque

def execute_example_stack():
  # 스택 구현
  stack = []
  
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()
  
  print("===== stack start =====")
  print(stack) # 최하단 원소부터 출력
  print(stack[::-1]) # 최상단 원소부터 출력
  print("===== stack end =====")

def execute_example_queue():
  # 파이썬으로 큐 구현할 때는 collections 모듈에서 제공하는 deque 자료구조 활용
  
  queue = deque()
  
  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()
  queue.append(1)
  queue.append(4)
  queue.popleft()
  
  print("===== queue start =====")
  print(queue) # 먼저 들어온 순서대로 출력
  queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
  print(queue) # 나중에 들어온 원소부터 출력
  print("===== queue end =====")
  
def execute_example_recursive_function(i):
  # 재귀함수 구현
  # 재귀함수: 자기 자신을 다시 호출하는 함수
  if i == 100:
    return
  print (i, ' 번 째 재귀 함수에서', i+1, ' 번 째 재귀 함수 호출')
  execute_example_recursive_function(i+1)
  print(i, ' 번 째 재귀 함수 종료')

def execute_example_factorial_iterative(n):
  # 반복적(iterative)으로 구현한다: 반복문을 이용하여 구현
  # 반복적으로 n! (n팩토리얼) 구현
  
  result = 1
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n+1):
    result *=i
  return result
  
def execute_example_factorial_recursive(n):
  # 재귀적(recursive)으로 구현한다: 반복적 구현과 대비되는 의미
  if n <= 1: # n이 1 이하인 경우 1을 반환
    return 1
  # n! = n * (n-1)!을 코드로 작성
  return n * execute_example_factorial_recursive(n-1)
  
#execute_example_stack()
#execute_example_queue()
#execute_example_recursive_function(1)

#print('반복적 구현: ', execute_example_factorial_iterative(5))
#print('재귀적 구현: ', execute_example_factorial_recursive(5))

# DFS
# Depth-First Search: 깊이 우선 탐색. 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘.
# 그래프의 기본 구조
# 그래프: 노드(Node)와 간선(Edge)으로 표현. 노드는 정점(Vertex)이라고도 말함.
# 그래프 탐색: 하나의 노드를 시작으로 다수의 노드를 방문하는 것.
# 두 노드가 간선으로 연결되어 있음 == 두 노드는 인접하다(adjacent)
#          노드
#   (간선) / \ (간선)
#      노드  노드
# (이런 그림처럼 생김)
# 그래프의 표현 방식
# 1. 인접 행렬 (Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
#
#         0
#      7 /\ 5
#      1   2
#     (그래프)
#
#   0   1   2
# 0 0   7   5
# 1 7   0  무한
# 2 5  무한 0
#
# 2차원 배열에 각 노드가 연결된 형태를 기록
# 파이썬에서는 리스트 자료형으로 표현 (다른 언어에서는 배열)
# 2차원 리스트로 구현
# 연결 되지 않은 노드끼리는 무한의 비용이라고 작성
# 무한의 비용 초기화는 보통 999999999 등의 값으로 초기화
# 코드 예시
# INF = 999999999 무한의 비용 선언
# graph = [
#    [0, 7, 5],
#    [7, 0, INF],
#    [5, INF, 0]
# ]

# 2. 인접 리스트 (Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식  
# 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
# 링크드 리스트 자료구조를 이용하여 구현
# C++, 자바 등에서는 별도 링크드 리스트 표준 라이브러리 이용
# 파이썬은 기본 자료형인 리스트 자료형이 append()와 메소드 제공
# 배열과 연결 리스트의 기능을 모두 기본으로 제공
# 즉 인접 리스트 이용하여 표현할 때에도 단순히 2차원 리스트를 이용하면 됨
# 코드 예시
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
# graph = [[] for _ in range(3)]
# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
# graph[0].append((1, 7))
# graph[0].append((2, 5))
# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
# graph[1].append((0, 7))
# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
# graph[2]. append((0, 5))

# DFS는 스택 자료구조를 이용.
# DFS의 구체적 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리.
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
# 참고: 방문 처리란 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것을 의미.
# 일반적으로, 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리한다. (관행적으로)

def execute_example_dfs(graph, v, visited):
 # 현재 노드를 방문 처리
 visited[v] = True
 print(v, end=' ')
 #현재 노드와 연결된 다른 노드를 재귀적으로 방문
 for i in graph[v]:
   if not visited[i]:
     execute_example_dfs(graph, i, visited)
     

# 각 노드가 연결된 정보를 이스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

#execute_example_dfs(graph, 1, visited)

# BFS
# 너비 우선 탐색: 가까운 노드부터 탐색하는 알고리즘
# DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작. BFS는 이와 반대.
# 구현 시 큐 자료구조를 이용
# 동작 방식
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
# 일반적인 경우 실제 수행시간은 DFS보다 좋은 편이라고 함.

def execute_example_bfs(graph, start, visited):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  
  # 현재 노드 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
# execute_example_bfs(graph, 1, visited)

# 실전문제
# n, m을 공백으로 구분하여 입력 받기
#n,m = map(int, input().split())

#print('얼음틀 크기: ', n, ' X ', m)

# 2차원 리스트 정보 입력 받기
#graph_practice = []
#for i in range(n):
#  graph_practice.append(list(map(int, input())))

#print(graph_practice)   

def practice_3(n,m):
  # n x m 크기의 얼음틀
  # 첫 번째 줄: 얼음틀의 세로 길이 n, 가로 길이 m (1<= n,m <= 1000)
  # 두 번째 줄 부터 n+1 번 째 줄 까지 얼음 틀의 형태
  # 이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1
  # 한 번에 만들 수 있는 아이스크림의 개수 출력
  
    
  # 모든 노드(위치)에 대하여 음료수 채우기
  result = 0
  for i in range(n):
    for j in range(m):
      # 현재 위치에서 DFS 수행
      # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
      if dfs(i,j) == True:
        result +=1
  
  # 정답 출력
  print(result)      
  
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우 즉시 종료 처리
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면 
  if graph_practice[x][y] == 0:
    # 해당 노드 방문 처리
    graph_practice[x][y] = 1
    # 상하좌우 위치도 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False
  
# practice_3(n,m)

# 첫째 줄에 두 정수 a, b (4<=a,b<=200)
# a 개 줄에 각각 b 개의 정수 (0이나1)로 미로 정보 입력
# 시작칸과 마지막칸은 항상 1
# 최소 이동 칸의 개수 출력

a, b = map(int, input().split())
miro = []
for i in range(a):
  miro.append(list(map(int, input())))
# 이동할 네 방향 정의 (상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def practice_4(x,y):
  queue = deque()
  queue.append((x,y))
  
  while queue:
    x,y = queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= a or ny >= b:
        continue
      #벽인 경우 무시
      if miro[nx][ny] == 0:
        continue
      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if miro[nx][ny] == 1:
        miro[nx][ny] = miro[x][y] + 1
        queue.append((nx, ny))
  #가장 오른쪽 아래까지의 최단거리 반환
  return miro[a-1][b-1]

print(practice_4(0,0))

  
