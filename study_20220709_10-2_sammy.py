"""
챕터 10 그래프이론

10-1 개선 부분

경로 압축 기법 소스코드
각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 로트 노드가 바로 부모 노드가 된다.
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]