"""
챕터 08 다이나믹 프로그래밍
바닥공사
: 가로N, 세로 2

바닥을 채우는 타일조합 모두의 경우의 수를 구하라
첫째 줄에 N이 주어진다.
첫째 줄에 2XN크기의 바닥을 채우는 방법의 수를 796,796을 나눈 나머지를 출력한다.
덮개는 1X2, 2X1, 2X2 크기의 3종류

힌트: 왼쪽부터 차례대로 바닥을 덮개로 채운다고 생각하기
"""

n=int(input())
d=[0]*1001

d[1]=1
d[2]=2

for i in range(3, n+1):
    d[1] = (d[i-1]+2 * d[i-2]) % 796796

print(d[n])
