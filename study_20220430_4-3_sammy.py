"""
구현
실전문제 3 왕실의 나이트
행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다.
이동 시 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

평면 상에서 위치가 주어졌을 때 이동할 수 있는 경우의 수를 출력하는 프로그램 작성하기
행 위치는 1~8로 표현하고 열 위치를 표현할 때는 a~h로 표현한다.

[입력조건]
첫째 줄에 8 X 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 열이 입력된다.
입력 문자는 a1처럼 열과 행으로 이뤄진다.
첫째 줄에 사람이 이동할 수 있는 경우의 수를 출력하시오.

입력예시 a1
출력예시 2

[참고]
ord(문자)
하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
ord('a')를 넣으면 정수 97을 반환합니다.

"""

# 현재 위치 입력받기
input_data = input()
column = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])

# 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
