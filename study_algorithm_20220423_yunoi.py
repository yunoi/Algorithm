# first commit test
import time

# 입출력
# 데이터의 개수 입력
# n = int(input())
# 각 데이터를 공백으로 구분하여 입력
# data = list(map(int, input().split()))

# import sys
# sys.stdin.readline().rstrip()

# 시간측정코드
# import time
# start = time.time() # 시작 시간 저장
# print (f'소요시간: {time.time() - start}') # 현재시간 - 시작시간 = 실행시간

### 3. 그리디
def execute_example(): 
  #### 예제 3-1 거스름돈
  # 동전 종류: 500, 100, 50, 10
  # 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수.
  # (단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.)

  # 1. 큰 동전으로 나눈다. -> 몫이 거슬러 줄 동전의 수
  # 2. 나머지 거스름돈을 다음 단위 동전으로 나눈다 -> 몫이 거슬러 줄 동전의 수
  # 3. 입력받은 잔돈 n이 0이 될 때까지 위 과정을 반복하여 계산
  
  # 예제3-1 내 풀이
  print('입력시작:')
  n = exam_n = int(input())

  start = time.time() # 시작 시간 저장
  # 거슬러 줄 각 동전의 수 변수 초기화
  r500 = r100 = r50 = r10 = 0 

  while n > 0:
    if n >= 500:
      r500 = n // 500
      n -= r500 * 500
    elif 500 > n >= 100:
      r100 = n // 100
      n -= r100 * 100
    elif 100 > n >= 50:
      r50 = n // 50
      n -= r50 * 50
    else:
      r10 = n // 10
      n -= r10 * 10
    
  print(f'거슬러줄 동전 개수: {r500+r100+r50+r10}개')
  print (f'소요시간: {time.time() - start}') # 현재시간 - 시작시간 = 실행시간

  # 3-1 답안예시
  exam_start = time.time()

  count = 0
  coin_types = [500, 100, 50, 10]

  for coin in coin_types:
    count += exam_n // coin
    exam_n %= coin

  print(count)
  print(f'예시 소요시간: {time.time() - exam_start}') # 현재시간 - 시작시간 = 실행시간

def execute_practice2():
  # 실전문제: 큰 수의 법칙
  # 다양한 수로 이루어진 배열이 있을 떄 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
  # 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
  # ex. 2,4,5,4,6으로 이로어진 배열이 있을 때 M = 8, K = 3이라고 가정.
  # 이 경우 특정 인덱스의 수가 연속해서 3번 까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는
  # 6+6+6+5+6+6+6+5 = 46이된다
  ### 아아 그러면 제일 큰 숫자를 일단 구해서 K번 더하고, 그 다음은 다음으로 큰 숫자 한번 더한 다음에
  ### 다시 젤 큰 숫자를 K번 더하기를 하면 되겠다. 이렇게 했는데 M번이 다 안되면 M번 채울 떄 까지 
  ### 다시 2등으로 큰 숫자를 한 번 더해주고 1등 숫자 K번 더하기를 반복하면 되겠다.
  # 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른것으로 간주한다. 
  ### 그니까 data[0] = data[2] = 4 에 제일 큰 수, 예를 들어 7이 있다 이러면 K가 3, M이 8일 떄
  ### 걍 4+4+4+4+4+4+4+4 가 가능하다는 얘기로구먼

  # 배열의 크기 n, 숫자가 더해지는 횟수 m, 그리고 k가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오

  # 입력조건 
  # 1. 첫째 줄에 n(2 <= n <= 1,000), m(1 <= m <= 10,000), k(1 <= k <= 10,000) 의 자연수가 주어지며, 각 자연수는 공백으로 구분
  # 2. 둘째 줄에 n개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.
  # 3. 입력으로 주어지는 k는 항상 m보다 작거나 같다.
  # 출력조건
  # 첫째 줄에 더해진 답 출력
  
  n,m,k = map(int, input().split())
  # m과 k의 관계 정리...
  # max_value를 k번 더하기를 최대한 하기 위해 m을 k로 나누어서 몫, 나머지를 구하자
  # m=8, k=3일 경우 몫은 2, 나머지 2
  # 즉 몫(max_value * k) + (나머지 * 두 번째로 큰 수)
  # 몫이나 나머지가 0이 나올 경우를 생각해야된다.
  # 몫이 0이 나오는 경우. 이 경우는 m이 k의 배수이니까... 연속으로 최댓값을 m회 더해버리는 계산이 나올 수 있다.
  # 그래서 result = a * (max_value * k) + (b * second_value) 이 로직은 그대로 사용할 수 없다
  # 중간에 한번 두 번째로 큰 수를 한 번 더해줘야한다.
  
  # 풀이 참고
  # 반복되는 수열이 힌트
  # 반복되는 수열의 길이 = k + 1
  # 이걸 이용해야 한다.
  # m을 k+1로 나눈 몫 = 수열이 반복되는 횟수 이용 
  # (m // k+1) * k 는 가장 큰 수가 등장하는 횟수
  # m을 k+1로 나눈 나머지가 있다면 이 나머지 만큼 최댓값이 추가로 더해진다.
  # 즉 가장 큰 수가 더해지는 횟수는
  # (m // (k+1)) * k + (m % k+1)

  # ################## 처음 풀이  
  # a = m // k
  # print(a)
  # b = m % k
  # print(b)
  
  # data =list(map(int, input().split()))
  # # case1: 제일 큰 수가 유일하게 존재한다.
  # # case2: 제일 큰 수가 중복되어 존재한다.
  # max_value = max(data)
  # print(max_value)
  # data.remove(max_value)
  # second_value = max(data) # remove를 하면 어차피 처음 하나 걸릴때만 지워질테니까 제일 큰 수가 중복되어도 동일 로직으로 처리가능해보임
   # print(second_value)
  # result = a * (max_value * k) + (b * second_value)
  # print(result)
  # ################## 다시 풀이  
  
  data =list(map(int, input().split()))
  max_value = max(data)
  data.remove(max_value)
  second_value = max(data) # remove를 하면 어차피 처음 하나 걸릴때만 지워질테니까 제일 큰 수가 중복되어도 동일 로직으로 처리가능해보임
  # 최댓값이 더해지는 횟수 계산
  count = (m // (k+1)) * k 
  count += m % (k+1)
  result = 0
  result += count * max_value # 가장 큰 수 더하기
  result += (m - count) * second_value # 두 번째로 큰 수 더하기
  print(result)
  
  ####################################################
  
  # 예시 풀이
  exam_data =list(map(int, input().split()))
  exam_data.sort() # 입력받은 수 정렬
  first = exam_data[n-1] # 가장 큰 수
  second = exam_data[n-2] # 두 번째로 큰 수
  
  exam_result = 0
  
  while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
      if m == 0: # m이 0이라면 반복문 탈출
        break
      exam_result += first
      m -= 1 # 더할 때마다 1씩 빼기 
    if m == 0: # m이 0이라면 반복문 탈출
      break
    exam_result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기
  
  print(exam_result)
  
def execute_practice3():
  # 실전문제: 숫자 카드 게임
  
  # 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.
  # 1. 숫자가 쓰인 카드들이  n x m 형태로 놓여있음. n: 행, m: 열
  # 2. 뽑고 싶은 카드가 포함되어 있는 행(n) 먼저 선택 
  # 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
  # 4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
  #    최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
  # 입력 조건
  # 첫째 줄에 숫자 카드들이 놓인 행의 개수 n과 열의 개수 m이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= n,m <= 100)
  # 둘째 줄 부터 n개의 줄에 걸처 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000이하의 자연수이다.
  # 출력 조건
  # 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
  
  # 예시 풀이
  # n,m을 공백으로 구분하여 입력받기
  n, m = map(int, input().split())
  
  result = 0
  # 한 줄씩 입력받아 확인
  for i in range(n):
    data=list(map(int, input().split()))  # m개로 한정하여 입력을 받도록 제한하지 않아도 되는구나... 
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data) # 이렇게 그냥 넣으면 된다고? 데이터타입이 잘 이해안됨.... 걍 넣으면 알아서 받는다는 게...
    print(f'{i}차 반복의 min_value: {min_value}')# 어떻게 들어가고있는지 찍어보자
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value) # 배열같은걸로 되어있는걸까... 
    # m 개의 값을 받는다. 그리고 나서 m개 중 최솟값을 찾고, '그걸 다른 변수에 넣어놓음' <- 이부분,,, 값이 갱신되는게 아니고 쌓인다는건가???
  print(result) # 최종 답안 출력
  
  ## 2중 반복문 구조를 이용한 풀이
  result2 = 0
  for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
      min_value = min(min_value, a)
    result2 = max(result2, min_value)
  print(result2)

def execute_practice4():
  # 실전문제: 1이 될 때까지
  # 어떤 수 n이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
  # 단 2번 연산은 n이 k로 나누어떨어질 때만 선택할 수 있따.
  # 1. n에서 1을 뺀다.
  # 2. n을 k로 나눈다.
  # 입력조건
  # n k (2 <= n,k <= 100,000) n은 항상 k보다 크거나 같다.
  
  # 1. 횟수를 세는 count 변수 선언
  # 2. 주어진 수 n이 1인지 체크하는 반복문을 작성
  # 3. 반복문 내부에서 n을 k로 나눴을 때 나머지가 0인지 확인
  # 4. 3이 True일 때는 2번 식 적용
  #    False일 때는 1번 식 적용
  # 5. count += 1
  # 6. 반복문 탈출 후 count 출력
  
  n,k = map(int, input().split())
  start = time.time()
  count = 0
  while n > 1:
    if n%k == 0:
      n //= k
    else:
      n -= 1
    print(n)
    count += 1
  print(count)
  print(f'소요시간: {time.time() - start}')
  
# execute_practice2() # 실전 2번 실행
# execute_practice3() # 실전 3번 실행
execute_practice4() # 실전 4번 실행
# 3 3
# 3 1 2
# 0차 반복의 min_value: 1
# 4 1 4
# 1차 반복의 min_value: 1
# 2 2 2
# 2차 반복의 min_value: 2
# 2

# 중간에 체크하느라 넣어놓은 print 구문을 빼면 한 줄씩 입력받아 확인이라는 의미가 이해된다.
# result를 반복문 밖에 미리 선언해놓은거 까먹었네... 
# 저기다 넣은 값은 일단 안변하니까 비교할 수 있다. min_value 값이 쌓여서 그것끼리 비교하는 것이 아님!!
# n이 3이라는 가정 하에
# 1차 입력 시작
# 일단 한 줄을 입력받고, 현재 줄에서 가장 작은 수를 min_value에다가 넣는다.
# 그 다음 result와 min_value를 비교해서 둘 중 큰 값을 result에 다시 넣는다.
# 2차 입력 시작
# 2차 입력 값들 중 최솟값을 min_value에 할당~~~ 이렇게 반복 진행한다. 마지막에 result를 출력하면 되는 것.


