"""
챕터 06 정렬

"""

array = [('바나나', 2), ('사과', 5),('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)

print(result)