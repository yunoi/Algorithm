"""
챕터 05 DFS/BFS 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

DFS: 스택, 재귀함수 이용
BFS: 큐, 큐 자료구조 이용

첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로
미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
첫째 줄에 최소 이동 칸의 개수를 출력한다.

BFS는 시작 시점에서 가까운 노드부터 차례대로 그래프의 모든 노트를 탐색
그러므로 (1, 1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.


"""
from collections import deque

#얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림 개수를 구하는 프로그램 작성
n, m = map(int, input().split())
#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이들의 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 소스코드 구현
def bfs(x, y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    #큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))