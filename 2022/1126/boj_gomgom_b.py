# B 붙임성이 좋은 총총이
target = set()
target.add('ChongChong')
answer = 1
for _ in range(int(input())):
    a, b = input().split()
    if a != b and a in target and b not in target:
        answer += 1
        target.add(b)
    elif a != b and b in target and a not in target:
        answer += 1
        target.add(a)
print(answer)