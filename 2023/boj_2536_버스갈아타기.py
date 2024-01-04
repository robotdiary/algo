from collections import deque
N, M = map(int, input().split())  # M, N 바꿔 받음
K = int(input())  # 버스 수
buses = {}
for _ in range(K):
    B, X1, Y1, X2, Y2 = map(int, input().split())  # 버스번호, 양끝좌표
    buses[B] = [X1, Y1, X2, Y2]
sx, sy, dx, dy = map(int, input().split())  # 출발지, 목적지

q = []
for key, value in buses.items():
    x1, y1, x2, y2 = value
    if