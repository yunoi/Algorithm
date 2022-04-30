# chapter 4. 구현
# 완전탐색, 시뮬레이션 유형 포함
# 완전 탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법.
# 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형.

# 파이썬 문법에 익숙해야 유리

from winreg import DisableReflectionKey


def execute_example1():
  # 예제 4-1 상하좌우
  # N X N 크기의 정사각형 공간이 주어짐.
  # 시작 좌표 (1, 1)
  # L, R, U, D (좌, 우, 상, 하)
  # ex. N = 5
  # (1,1) (1,2) (1,3) (1,4) (1,5)
  # (2,1) (2,2) (2,3) (2,4) (2,5)
  # (3,1) (3,2) (3,3) (3,4) (3,5)
  # (4,1) (4,2) (4,3) (4,4) (4,5)
  # (5,1) (5,2) (5,3) (5,4) (5,5)
  # 계획서: R R R U D D (정사각형 공간을 벗어나는 계획은 무시된다.)
  # 우측으로 3번 움직인 후 위로 1번, 아래로 두 번 움직였을 떄 도착하는 좌표는
  # (1,2) (1,3) (1,4), U는 무시, (2.4) (3,4) => 최종 (3,4)

  # 입력조건
  # 첫째 줄에 N (1 <= N <= 100)
  # 둘째 줄에 계획서 내용 (1 <= 이동 횟수 <= 100)
  # 출력 조건
  # 최종 좌표를 공백으로 구분하여 출력: X Y

  # (X, Y)
  # 시작은 항상 (1,1)
  # 시작일 때: L: 무시, R: Y+1, U: 무시, D: X+1

  # 답안 예시
  n = int(input())
  x, y = 1, 1
  plans = input().split()
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  move_types = ['L', 'R', 'U', 'D']

  for plan in plans:
    for i in range(len(move_types)):
      if plan == move_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    x, y = nx, ny

  print(x, y)

def execute_example2():
  # 예제 4-2 시각
  # 정수 N 입력
  # 00시 00분 00초 ~ N시 59분 59초 까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
  # ex. N = 1 일 때 00시 00분 03초, 00시 13분 30초... 등
  # 입력 조건 0 <= N <= 23

  h = int(input())

  count = 0
  for i in range(h+1):
    for j in range(60):
      for k in range(60):
        # 매 시각 안에 3 이 포함되어 있다면 카운트+1
        if '3' in str(i)+str(j)+str(k):
          count += 1

  print(count)
  

def execute_practice1():
  # 나이트가 어떤 특정 위치에 있을 떄 이동할 수 있는 경우의 수를 구할 것
  # 열은 a~h
  # 행은 1~8
  # 체스 판 밖으로 이동할 수 없다.
  
  # 나이트의 현재 위치 입력
  position = input()
  row = int(position[1])
  # ord(문자)
  # 하나의 문자를 인자로 받고 인자에 해당하는 유니코드 정수를 반환
  # ex. ord('a')의 반환값은 97
  # a가 가장 작은 값이므로 들어오는 값에서 a를 빼주면 1부터 시작할 수 있다.
  column = int(ord(position[0])) - int(ord('a')) + 1
  
  # 나이트가 이동 가능한 8가지 방향 정의
  steps = [(-2,-1), (-1,-2), (1,-2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
  
  # 8가지 방향에 대해 각 위치로 이동 가능한지 확인
  result = 0 # 경우의 수를 센다
  for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하면 result + 1
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
      result += 1
  
  print(result)
  
  
def execute_practice2():
  # 실전문제 3 게임 개발
  # 캐릭터가 있는 장소 1 X 1 정사각형으로 이루어진 N X M 크기의 직사각형 맵
  # 각 칸은 육지 또는 바다.
  # 캐릭터는 동서남북 중 한 곳을 바라본다.
  # 맵의 각 칸 표시 (A, B)
  # A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수
  # => 기준이 북, 서라는 뜻인 듯. 북쪽에서 남쪽으로 갈 수록 1 씩 증가, 서에서 동으로 갈 수록 1 씩 증가
  # 이동가능 방향은 상하좌우. 바다로 되어있는 곳은 갈 수 없음.
  
  # 캐릭터 움직임 설정을 위한 매뉴얼
  # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
  # 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
  #     왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
  # 3. 만약 네 방향 모두 이미 가본 칸이거나 바다 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
  #     단, 이때 뒤쪽 방향이 바다 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
  
  # 매뉴얼에 따라 캐릭터를 이동시킨 뒤에 캐릭터가 방문한 칸의 수를 출력할 것.
  
  # 입력 조건
  # 첫째 줄: 맵의 세로 크기 N 가로크기 M (3 <= N, M <= 50)
  # 둘째 줄: 게임 캐릭터가 있는 칸의 좌표 (A, B) 바라보는 방향 d (0: 북, 1: 동, 2: 남, 3: 서)
  # 셋째 줄: 맵이 육지인지 바다인지에 대한 정보. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
  #           맵의 외곽은 항상 바다로 되어있다. (0: 육지, 1: 바다)
  # 캐릭터의 처음 위치 칸의 상태는 항상 육지이다.
  # 입력 예시
  # 4 4           (4 X 4 맵 생성)
  # 1 1 0         (1,1)에 북쪽(0)을 바라보며 서 있는 캐릭터
  # 1 1 1 1       첫 줄은 모두 바다
  # 1 0 0 1       둘째 줄은 바다/육지/육지/바다
  # 1 1 0 1       셋째 줄은 바다/바다/육지/바다
  # 1 1 1 1       넷째 줄은 모두 바다
  
  # 2차원 리스트 초기화시 리스트 컴프리헨션 문법? -> 부록 A 확인할 것
  
  # 맵 크기 입력받기
  n, m = map(int, input().split())
  
  # 방문한 위치를 저장하기 위한 맵 생성하여 0으로 초기화
  d = [[0] * m for _ in range(n)]
  
  # 현재 캐릭터가 위치하는 좌표 x, y 와 방향 입력받기
  x, y, direction = map(int, input().split())
  # 현재 좌표 방문 처리
  d[x][y] = 1
  
  # 전체 맵 정보 입력받기
  array = []
  for i in range(n):
    array.append(list(map(int, input().split())))
    
  # 북, 동, 남, 서 방향 정의
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  
  # 왼쪽으로 회전 함수
  def turn_left():
    global direction
    direction -= 1
    if direction == -1:
      direction = 3
    
  count = 1
  turn_time = 0
  while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동 처리
    if d[nx][ny] == 0 and array[nx][ny] == 0:
      d[nx][ny] = 1
      x = nx
      y = ny
      count += 1
      turn_time = 0
      continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else: 
      turn_time += 1
    # 네 방항 모두 갈 수 없는 경우
    if turn_time == 4:
      nx = x - dx[direction]
      ny = y - dy[direction]
      # 뒤로 갈 수 있다면 이동하기
      if array[nx][ny] == 0:
        x = nx
        y = ny
      # 뒤가 바다로 막혀있는 경우
      else:
        break
      turn_time = 0
      
  # 출력
  print(count)
  

      
############################################################
# execute_example1()
# execute_example2()
# execute_practice1()
# execute_practice2()

# 맵 크기 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터가 위치하는 좌표 x, y 와 방향 입력받기
x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))
  
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 함수
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3
  
count = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동 처리
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else: 
    turn_time += 1
  # 네 방항 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0
    
# 출력
print(count)
