def push(item, size): # 사이즈가 꼭 있어야 하나? 전체 사이즈에서 제한된 만큼만 가고싶을 때는 쓸 수 있다.
    global top
    top += 1
    if top == size: # 사이즈 넘어가는 걸 빼줘야한다.
        print('overflow!')
    else:
        stack[top] = item

def pull():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        result = stack[top]
        stack[top] = 0
        top -= 1
        return result # return하면 함수가 끝나니까 인덱스 먼저 줄이고 +1인덱스를 뽑는다.

# 빈 스택 칸
size = 10
stack = [0] * size
top = -1
# 스택 수정
push(1, 2)
push(2, 3)
push(3, 4)
print(pull())
print(top)
print(pull())
print(stack[top])
print(stack)

