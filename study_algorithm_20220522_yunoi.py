# 챕터 6. 정렬

# 정렬: 데이터를 특정한 기준에 따라서 순서대로 나열하는 것. (ex. 오름차순, 내림차순 등)
# 종류: 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬

# 선택 정렬
# 주어진 데이터 중 매번 가장 작은 것을 선택하여 정렬

def selection_sort_ex(): 
  array = [7,5,9,0,3,1,6,2,4,8]
  
  print('before sort: ',array)
  
  for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스 저장
    for j in range(i+1, len(array)):
      if array[min_index] > array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프: 두 변수의 위치를 변경하는 작업
  
  print(array)
  
#selection_sort_ex()

# 참고: 스와프 소스코드
# 다른 언어에서는 '음료를 서로 바꾸어 담기 로직'을 사용
def swap_ex():
  # 0 인덱스와 1 인덱스의 원소 교체하기
  array = [3, 5]
  array[0], array[1] = array[1], array[0]
  
  print(array)

# swap_ex()

# 삽입정렬
# 데이터를 하나씩 확인하며 적절한 위치에 삽입.
# 선책 정렬보다 실행 시간 측면에서 더 효율적
# 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 효율적

def insertion_sort_ex():
  array = [7,5,9,0,3,1,6,2,4,8]
  
  for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
      if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
        array[j], array[j-1] = array[j-1], array[j]
      else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        break
      
  print(array)

#insertion_sort_ex()

# 퀵정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 교환
# 피벗: 교환하기 위한 '기준'
# 퀵 정렬 수행 전에 피벗을 어떻게 설정할 것인지 미리 명시해야 함
# 피벗을 설정하고 리스트를 분할한는 방법에 따라서 퀵 정렬을 구분함
# 가장 대표적인 분할 방식은 호어 분할
# 호어 분할 방식의 피벗 설정 규칙: 리스트에서 첫 번째 데이터를 피벗으로 설정
# 피벗 설정 후 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾음
# 그다음 큰 데이터와 작은 데이터의 위치 서로 교환하는 과정 반복

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort_ex(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      right -= 1
    if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 아니라면 작은 데이터와 큰 데이터 교체
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분, 오른쪽 부분 각각 정렬 수행
  quick_sort_ex(array, start, right -1)
  quick_sort_ex(array, right +1, end)

# quick_sort_ex(array, 0, len(array)-1)
# print(array)

# 계수 정렬
# 특정 조건이 부합할 때만 사용 가능하지만 매우 빠른 정렬 알고리즘
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 백만을 넘지 않을 때 효과적으로 사용 가능
# 계수 정렬을 이용할 때 '모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언'해야 하기 때문
# 직접 데이터의 값을 비교한 뒤에 위치를 변경하여 정렬하는 방식이 아님
  
def count_sort_ex():
  # 모든 원소의 값이 0보다 크거나 같다고 가정
  array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
  # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
  count = [0] * (max(array)+1)
  
  for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
  for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
      print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
      
#count_sort_ex()      

def sort_practice_1():
  n = int(input())
  array = []
  
  for i in range(n):
    array.append(int(input()))
    
  count = [0] * (max(array)+1)
  #print(array)
  #print(count)
  
  for i in range(len(array)):
    count[array[i]] += 1
  
  for i in reversed(range(len(count))):
    for j in range(count[i]):
      print(i, end=' ')
      
#sort_practice_1()

def or_sort_practice_1():
  n = int(input())
  
  array = []
  for i in range(n):
    array.append(int(input()))
    
  # 파이썬 기본 정렬 라이브러리 이용하여 정렬 수행
  array = sorted(array, reverse=True)
  
  # 결과 출력
  for i in array:
    print(i, end=' ')

# or_sort_practice_1()

def sort_practice_2():
  # n명의 학생정보
  # 학생 정보는 학생의 이름과 성적으로 구분
  # 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름 출력
  
  n = int(input())
  
  array = []
  for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))
  #print(array)  
  # 키를 이용하여 점수 기준으로 정렬
  array = sorted(array, key=lambda student: student[1]) # def 함수명(매개변수): return 결과 -> 람다표현식으로는 'lambda 매개변수: 결과' 로 표현

  for student in array: # 람다식 반환값 이용
    print(student[0], end=' ')

# sort_practice_2()

def sort_practice_3():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  
  a.sort()
  b.sort(reverse=True)
  
  # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
  for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
      # 두 원소를 교체
      a[i], b[i] = b[i], a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때 반복문 탈출
      break
  
  print(sum(a))
  
sort_practice_3()