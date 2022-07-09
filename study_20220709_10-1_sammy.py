"""
챕터 10 그래프이론

인접 행렬: 2차원 배열을 사용하는 방식
인접 리스트: 리스트를 사용하는 방식

서로소 집합: 공통 원소가 없는 두 집합
1. union: 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
2. find: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
서로소 집합 자료구조는 union-find(합치지 찾기) 자료구조
트리 자료구조를 이용하여 집합을 표현

"""

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        return find_parent(parent, parent[x])
    return x

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b] =a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent=[0]*(v+1) # 부모 테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] =1

#union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블: ', end=' ' )
for i in range(1,v+1):
    print(parent[i], end=' ')