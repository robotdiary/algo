keyboard = {0: 'qwert', 1: 'asdfg', 2: 'zxcv', 3:'#yuiop', 4:'#hjkl', 5:'bnm'}
left = [0, 0]
right = [0, 0]
l, r = input().split()
for i in range(3):
    if l in keyboard[i]:
        left = [i, keyboard[i].index(l)]
    if r in keyboard[i + 3]:
        right = [i + 3, keyboard[i + 3].index(r)]
answer = 0
for char in input():
    for j in range(3):
        if char in keyboard[j]:
            answer += abs(left[0] - j) + abs(left[1] - keyboard[j].index(char))
            left = [j, keyboard[j].index(char)]
            break
        elif char in keyboard[j + 3]:
            answer += abs(right[0] - (j + 3)) + abs(right[1] - keyboard[j + 3].index(char))
            right = [j + 3, keyboard[j + 3].index(char)]
            break
    answer += 1

print(answer)