# 종이 자르기
w, h = map(int, input().split())
width, height = [0, w], [0, h]
answer = 0

for i in range(int(input())):
    direction, location = map(int, input().split())
    if direction:  # 세로로
        width.append(location)
    else:
        height.append(location)
width.sort()
height.sort()

for r in range(len(width) - 1):
    row = width[r + 1] - width[r]
    for c in range(len(height) - 1):
        answer = max(answer, row * (height[c + 1] - height[c]))

print(answer)
