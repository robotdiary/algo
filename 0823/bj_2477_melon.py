# 백준 2477 참외밭 11:10~
k = int(input()) # 참외개수
# 1 오른쪽으로 2 왼쪽으로 3 아래로 4 위로
w = []
h = []
arr = [[0] * 500 for _ in range(500)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
stack = []
for tc in range(1, 7): # 1
    d, n = map(int, input().split()) # 4 50
    stack.append((d, n))
stack.reverse()
d, n = stack.pop() # 1 60
r, c = 0, 0 # 현재 위치
if d == 1:
    arr[0][0:n] = 1
    r, c = 0, n
elif d == 2:
    r, c = 0, n
elif d == 3:
    r, c = 0, 0
else:
    r, c = n, 0
while stack:
    arr[r][c]

print(stack)