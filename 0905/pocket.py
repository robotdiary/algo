import math

angle = 0.0
power = 0.0

target = [0, 0]
for ball in balls:
    if ball[0] >= 0 and ball[1] >= 0:
        target = ball

# whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
whiteBall_x = balls[0][0]
whiteBall_y = balls[0][1]

# targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
targetBall_x = target[0]
targetBall_y = target[1]

# width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
width = abs(targetBall_x - whiteBall_x)
height = abs(targetBall_y - whiteBall_y)


# 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
if whiteBall_x == targetBall_x:
    if whiteBall_y < targetBall_y:
        angle = 0
    else:
        angle = 180
elif whiteBall_y == targetBall_y:
    if whiteBall_x < targetBall_x:
        angle = 90
    else:
        angle = 270
    
# 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
if whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
    # 0, 127

    radian = math.atan(target[0] / 127-target[1])
    quest = [0, 0]
    quest[0] = target[0] + 5.73 * math.sin(radian)
    quest[1] = target[1] + 5.73 * math.cos(radian)
    width = abs(quest[0] - whiteBall_x)
    height = abs(quest[1] - whiteBall_y)
    radian2 = math.atan(width / height)
    angle = (180 / math.pi * radian2) + 270

# 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
elif whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
    radian = math.atan(width / height)
    angle = (180 / math.pi * radian)

# 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
    radian = math.atan(width / height)
    angle = (180 / math.pi * radian) + 180

# 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 90
    
# distance: 두 점(좌표) 사이의 거리를 계산
distance = math.sqrt(width**2 + height**2)

# power: 거리 distance에 따른 힘의 세기를 계산
power = distance * 0.5