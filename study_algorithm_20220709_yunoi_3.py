# 챕터 10 (계속)
# 신장 트리
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘
# 가능한 한 최소한의 비용으로 신장 트리를 찾는 대표적인 알고리즘
# 모든 간선에 대해 정렬 수행 후 가장 거리가 짧은 간선부터 집합에 포함.
# 사이클을 발생시킬 수 있는 간선의 경우는 포함시키지 않음
# 최소 신장 트리는 최종적으로 간선의 개수가 노드의 개수 - 1 과 같다는 특징이 있다.
# (트리 자료구조는 노드가 n개일 때 항상 간선의 개수가 n-1개이다)

# 크루스칼 알고리즘
from tkinter import E


def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else: 
    parent[a] = b

print('노드 개수, 간선 개수 입력')
node, edge = map(int, input().split())
parent = [0] * (node+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, node+1):
  parent[i] = i
  
# 모든 간선에 대한 정보 입력
print('모든 간선에 대한 정보 입력')
for _ in range(edge):
  a, b, cost = map(int, input().split()) 
  # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost, a, b))
  
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for e in edges: 
  cost, a, b = e
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print('최종 비용: ', result)
  
  