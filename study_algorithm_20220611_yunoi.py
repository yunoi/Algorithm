# 챕터 7. 이진 탐색

# 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.

# 순차 탐색 예시
def sequential_search(n, target, array):
  # 각 원소를 하나씩 확인
  for i in range(n):
    # 현재 원소가 찾는 원소와 동일한 경우
    if array[i] == target: 
      return i+1 # 현재 위치 반환
    
# print("생성할 원소 개수 입력")
# n = int(input())
# print("검색어 입력")
# target = input()
# print("원소 개수만큼 문자열 입력")
# array = input().split()

#순차 탐색 수행 결과 출력
# print("검색어 위치: ", sequential_search(n,target,array))

# 이진 탐색: 반으로 쪼개면서 탐색하기. 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교.
# 미리 정렬되어있어야 함.
# 구현 방법 1. 재귀 함수 이용, 2. 단순 반복문 이용

# 재귀 함수로 이진 탐색 구현
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  
  # 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid + 1, end)
   
# 원소 개수 n 과 찾고자 하는 문자열 target 입력받기
#n, target = list(map(int, input().split()))
# 전체 원소 입력받기
#array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#    print("원소가 존재하지 않습니다.")
# else:
#   print(result + 1)
  
# 반복문으로 이진 탐색 구현
def binary_search_using_loop(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return None

# 이진 탐색 수행 결과 출력
# result = binary_search_using_loop(array, target, 0, n - 1)
# if result == None:
#    print("원소가 존재하지 않습니다.")
# else:
#   print(result + 1)
  
# 트리 자료구조
# 그래프 자료구조의 일종. 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용.
# 노드와 노드의 연결로 표현. 
# 노드: 정보의 단위. 어떠한 정보를 가지고 있는 개체. 그래프의 노드와 동일한 개념.
# 주요 특징
#### 트리는 부모 노드와 자식 노드의 관계로 표현된다.
#### 트리의 최상단 노드를 루트 노드라고 한다.
#### 트리의 최하단 노드를 단말 노드라고 한다.
#### 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.
#### 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

# 이진 탐색 트리
# 트리 자료구조 중 가장 간단한 형태.
# 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조.
# 이진 탐색 트리의 특징
#### 부모 노드보다 왼쪽 자식 노드가 작다.
#### 부모 노드보다 오른쪽 자식 노드가 크다.
#### 왼쪽 자식 노드 < 부모노드 < 오른쪽 자식 노드가 성립.

# 이진 탐색 트리에서 데이터를 조회하는 과정
# 1. 루트 노드부터 방문 -> 찾는 값과 비교 -> 루트 노드가 찾는 값보다 작으면 오른쪽 노드 방문, 크면 왼쪽 노드 방문
# 2. 방문한 노드가 부모 노드가 되고, 1과 동일하게 비교하여 동일한 원소를 찾을 때까지 방문 반복

# 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이므로 입력이 빨라야 함.
## input() 함수 대신 sys 라이브러리의 readline() 함수를 이용하여 시간 초과를 피해야 한다.

# sys 라이브러리: 한 줄씩 입력 받음.
import sys
# 하나의 문자열 데이터 입력받기
#input_data = sys.stdin.readline().rstrip() # 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야 함
## readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하는 용도

# 입력받은 문자열 그대로 출력
#print(input_data)

# 실전문제
def binary_search_practice(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1 
  return None

# 가게 부품 개수 입력
# n = int(input())
# # 부품 번호 입력
# array = list(map(int, input().split()))
# array.sort() # 사전에 정렬 수행
# # 확인이 필요한 부품 개수 입력
# m = int(input())
# # 확인하려는 전체 부품 번호 입력
# request_number = list(map(int, input().split()))

# # 확인 요청 부품 번호 하나씩 확인
# for i in request_number:
#   # 해당 부품이 존재하는지 확인
#   result = binary_search_practice(array, i, 0, n - 1)
#   if result != None:
#     print('yes', end=' ')
#   else:
#     print('no', end=' ')
    
# 계수 정렬 예시
# 가게 부품 개수 입력
# n = int(input())
# array = [0] * 1000001

# 가게이 있는 전체 부품 번호를 입력받아서 기록
# for i in input().split():
#   array[int(i)] = 1

# 확인 요청한 부품 개수 입력
# m = int(input())
# 확인 요청 전체 부품 번호를 공백으로 구분하여 입력
# x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
# for i in x:
#   # 해당 부품이 존재하는지 확인
#   if array[i] == 1:
#     print('yes', end=' ')
#   else:
#     print('no', end=' ')

# 집합 자료형을 이용한 코드 예시
# n_set = int(input())
# array_set = set(map(int, input().split()))
# m_set = int(input())
# x_set = list(map(int, input().split()))

# for i in x_set:
#   if i in array_set:
#     print('yes', end=' ')
#   else:
#     print('no', end=' ')
  

# 실전문제 3

# 파라메트릭 서치: 최적화 문제를 결정 문제(예 혹은 아니오로 답하는 문제)로 바꾸어 해결하는 기법
# 일반적으로 반복문을 이용해 이진 탐색을 구현하면 간결해진다.

# 떡의 개수(n)와 요청한 떡의 길이(m) 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while(start<=end):
  total = 0
  mid = (start+end) // 2
  for x in array:
    # 잘랐을 때 떡의 양 계산
    if x > mid:
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total < m:
    end = mid -1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid # 최대한 덜 잘랐을 떄가 정답이므로, 여기에서 result에 기록
    start = mid + 1

print(result)