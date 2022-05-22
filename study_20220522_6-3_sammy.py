"""
챕터 06 정렬

삽입정렬
: 데이터가 거의 정렬되어 이을 때 효율적
  첫번째 데이터는 그 자체로 정렬되어있다고 판단하기 때문에 두번째 데이터부터 시작
  오름차순일때는 첫번째 데이터의 왼쪽에 삽입
  내림차순일 경우에는 첫번째 데이터의 오른쪽에 삽입
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스의 i부터 1까지 감소하며 반복하는 문법(start, end, step)
        if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
            array[j], array[j -1] = array[j -1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
