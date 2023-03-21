def push(item, size):
    global top
    top += 1
    if top > size:
        print('overflow')
    else:
        stack[top] == item
def pull():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        result = stack[top]
        stack[top] = 0
        top -= 1
        return result

T= int(input())
for tc in range(1, T+1):
    check = input()
    left = check.count('(')
    right = check.count(')')
    if left == right:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} -1')
