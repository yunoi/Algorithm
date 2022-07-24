# 챕터 10 그래프이론 실전문제 2

# 도시 분할 계획

# 입력
# 집 개수 n, 길 개수 m 
# 그 다음 m 줄에 걸쳐 길 정보가 a b c 세 개의 정수로 입력
# a번 집과 b번 집을 연결하는 길의 유지비가 c
# 출력
# 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값 출력

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
# 집 개수, 길 개수 입력
n, m = map(int, input().split())
parent = [0] * (n+1)

# 모든 길을 담을 리스트, 최종비용 담을 변수
road = []
result = 0

for i in range(1, n+1):
  parent[i] = i
  
# 모든 길 정보 입력
for _ in range(m):
  a, b, c = map(int, input().split())
  
  # 비용(c) 순으로 정렬 위해 튜플의 첫 번째 원소를 비용으로 설정
  road.append((c,a,b))
  
# 길을 비용순으로 정렬
road.sort()
last = 0 # 최소 신장 트리에 포함되는 길 중에서 가장 비용이 큰 길

# 길 하나씩 확인
for r in road:
  c, a, b = r
  # 사이클이 발생하지 않는 경우에만 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += c
    last = c
    
print(result - last)
  