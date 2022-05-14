"""
챕터 05 DFS/BFS 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

append() 리스트의 가장 뒤쪽에 데이터를 삽입
pop() 리스트의 가장 뒤쪽에서 데이터를 꺼냄

"""
stack = []

#삽입 - 삽입 - 삽입 - 삽입 - 삭제 - 삽입 - 삽입 - 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력 [5, 2, 3, 1]
print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]
