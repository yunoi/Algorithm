"""
실전문제 3
숫자카드게임: 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.
1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로
가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

HINT: 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾기
조건:
1<= N, M <= 100
둘째 줄부터 N개의 줄에 걸쳐 카드에 적인 숫자가 주어진다. 각 숫자는 1 이상 10,000이하의 자연수이다.

출력조건: 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
"""

# 방법 1
"""
n, m = map(int, input().split())
result = 0
#한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
"""
# 방법 2
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001  # 조건에서 1<= N, M <= 100
    for a in data:
        min_value = min(min_value, a)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
