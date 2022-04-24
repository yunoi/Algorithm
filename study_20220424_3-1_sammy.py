"""
예제 3-1
거스름돈: 거스름돈으로 500원, 100원, 50원 10원짜리 동전 존재
손님에게 거슬러 줘야 할 돈이 N워일때 거슬러 줘야 할 동전의 최소 개수
단, 거슬러줘야 할 돈 N은 할상 10의 배수
HINT: 가장 큰 화페 단위부터 돈을 거슬러주기
WHY Gird: 가지고 있는 동전 중에서 가장 큰 단위가 항상 작은 단위의 배수이므로 작은 단위들의 동전들을 종합해 다른 해가 나올 수 없기 때문
"""
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거술러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
