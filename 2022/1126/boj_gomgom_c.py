# C번 곰곰이와 학식
gom = list(map(int, input().split()))  # 곰곰이들
bob = list(map(int, input().split()))  # 식권
answer = 0
for i in range(3):
    if bob[i] >= gom[i]:
        answer += gom[i]
        bob[i] -= gom[i]
        gom[i] = 0
    else:
        answer += bob[i]
        gom[i] -= bob[i]
        bob[i] = 0

while bob[1] >= 3 or bob[2] >= 3 or bob[0] >= 3:
    for j in range(3):
        if bob[j] > 2:
            bob[(j + 1) % 3] += (bob[j] // 3)
            bob[j] %= 3
            if bob[(j + 1) % 3] >= gom[(j + 1) % 3]:
                answer += gom[(j + 1) % 3]
                bob[(j + 1) % 3] -= gom[(j + 1) % 3]
                gom[(j + 1) % 3] = 0
            else:
                answer += bob[(j + 1) % 3]
                gom[(j + 1) % 3] -= bob[(j + 1) % 3]
                bob[(j + 1) % 3] = 0
# print(gom)
# print(bob)
print(answer)