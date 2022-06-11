"""
챕터 07 순차 탐색
실전문제 부품찾기

N개의 부품, 각 부품은 정수 형태의 고유한 번호 존재
M개의 부품 주문
해당 부품들이 있는지 확인하는 프로그램 작성

입력조건
1. 첫째 줄에 정수 N이 주어진다.
2. 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
3. 셋째 줄에는 정수 M이 주어진다.
4. 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.

출력조건
1. 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력한다.
"""

#이진탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end ) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
        return None


    #N(가게의 부품 개수)입력
    n = list(input())
    array = list(map(int, input().split()))
    array.sort()
    m=int(input())

    x = list(map(int, input().split()))

    for i in x:
        result = binary_search(array, i, 0, n-1)
        if result != None:
            print('yes', end = ' ')
        else:
            print('no', end=' ')
