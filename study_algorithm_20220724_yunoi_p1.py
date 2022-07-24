# 챕터 10 그래프이론 실전문제 1

# 팀 결성
# 팀 합치기 연산: 두 팀을 합치는 연산
# 같은 팀 여부 확인 연산: 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산

# n, m 팀 번호, 연산 개수
# 다음 m 개 줄에는 각각의 연산 입력
# 팀 합치기 연산은 0 a b 형태. a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미.
# 같은 팀 여부 확인 연산은 1 a b 형태. a번 학생과 b번 학생이 같은 팀인지 확ㅇ니하는 연산
# a 와 b 는 n 이하의 양의 정수.
# 같은 팀 여부 확인 연산에 대해 한 줄에 하나씩 yes or no로 결과 출력

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x: 
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 팀 합치기
def union_team(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블상애서, 부모를 자기 자신으로 초기화
for i in range(0, n+1):
  parent[i] = i

# 각 연산 하나씩 확인
for i in range(m):
  oper, a, b = map(int, input().split())
  # 팀 합치기 연산일 때
  if oper == 0:
    union_team(parent, a, b)
  elif oper == 1 : # 찾기 연산일 떄
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')