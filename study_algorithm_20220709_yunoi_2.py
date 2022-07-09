# 개선된 서로소 집합 알고리즘

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
    
# 노드 개수, 간선 개수 입력
print('노드, 간선 개수 입력')
node, edge = map(int, input().split())
parent = [0] * (node+1)

for i in range(1, node+1):
  parent[i] = i
  
print('입력')
for i in range(edge):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
  
print('각 원소가 속한 집합: ', end='')
for i in range(1, node+1):
  print(find_parent(parent, i), end=' ')

print()
print('부모 테이블: ', end='')
for i in range(1, node+1):
  print(parent[i], end=' ')

