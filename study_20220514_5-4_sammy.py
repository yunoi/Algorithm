"""
챕터 05 DFS/BFS 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

"""
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 자귀 함수를 종료합니다.')

recursive_function(1)