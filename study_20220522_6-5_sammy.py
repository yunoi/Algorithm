"""
챕터 06 정렬

퀵정렬
: 가장 많이 사용됨
  기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
  피벗이 사용됨(큰 수와 작은 수를 교환할 때 교환하기 위한 기준을 피벗이라고 함)
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
   
print(quick_sort(array))