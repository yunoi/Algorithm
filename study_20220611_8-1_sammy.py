"""
챕터 08 다이나믹 프로그래밍

중복되는 연산을 줄이자
피보나치 수열
"""

def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x -1) + fibo(x -2)

print(fibo(4))
