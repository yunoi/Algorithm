"""
챕터 05 DFS/BFS 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

BFS: queue 가까운 노트부터 탐색, 큐 자료구조 이용, DFS와 반대
선입선출
"""

#BFS 메서드 정의, 너비 우선 탐색: 가까운 노드부터 탐색
from collections import deque

def bfs(graph, start, visited):
    #큐(queue)구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
              queue.append(i)
              visited[i] = True


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 연결된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)