#2022/04/16 study note

a = [1,2,3,4,5]
print(a)

print(a[0])

b = list()
print(b)

c = []
print(c)

print(a[-1])
print(a[1:4])

array = [i for i in range(20) if i % 2 == 1]
print(array)

another_array = []
for i in range(20):
  if i%2 == 0:
    another_array.append(i)
    
print(another_array)

#remove_all 구현
print("############ remove all ##########")
d = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)

# 튜플은 한번 선언된 값을 변경할 수 없다. -> 대입 연산자를 사용하여 값을 변경할 수 없다.
# 리스트는 대괄호를 이용하지만, 튜플은 소괄호를 이용한다.

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)
print(data['사과'])
if '바나나' in data:
  print("바나나 있다")

# 학생의 번호가 1부터 10000000까지로 구성되어있는 상황에서 최대 10000명의 학생을 선택했다.
# 이후 특정 학생 번호가 주어졌을 때 해당 학생이 선택되었는지를 어떻게 빠르게 알 수 있을까?
# 만약 리스트를 이용한다면, 1부터 천만까지의 각 번호가 선택되었는지를 저장할 수 있는 리스트를 만들어야 한다.
