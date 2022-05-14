"""
챕터 05 DFS/BFS 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 3 7 1 4
queue.reverse()
print(queue) # 4 1 7 3