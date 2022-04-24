"""
실전문제 2 
큰 수의 법칙: 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
ex) 3, 4, 3, 4, 3 여기서 첫번째 3과 세번째 3은 숫자는 같지만 서로 다른 것으로 간주
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 연속 제한 수 K

[입력 조건]
1. 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 이루어진다.
3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.
[출력조건]
1. 첫쨰 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
[입력예시]
5 8 3
2 4 5 4 6
[출력예시]
46
"""

# 방법1
"""
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 가장 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if (m == 0):  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기

    if (m == 0):  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)
"""

# 방법 2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k  # 가장 큰 수가 더해지는 횟수 계산
count += m % (k + 1)

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)