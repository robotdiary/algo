# 4874 Forth (D2)
def forth(line): # [5 3 * + .]
    stack = [] # [5, 3]
# [1] 리스트에서 원소 자체를 뽑아서 돈다
    for i in line: # *
# [2] 숫자면 스택에 넣는다.
        if i.isdigit():
            stack.append(i)
# [3] '.'이면 연산을 끝낼건데, 스택에 답 하나뿐이면 출력, 아니면 에러
        elif i == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
                return
            else:
                print(f'#{tc} error')
                return
# [4] '연산자'면 스택에서 두 개를 꺼내서 연산한다. 스택에 숫자가 없으면 에러
        else:
            if len(stack) > 1:
                num2 = int(stack.pop()) # 뒤에 걸 뒤에 연산
                num1 = int(stack.pop())
                new_num = 0
                if i == '+':
                    new_num = num1 + num2
                elif i == '-':
                    new_num = num1 - num2
                elif i == '*':
                    new_num = num1 * num2
                elif i == '/':
                    new_num = num1 // num2 # / 하면 .0으로 답이 나와서 틀리나봐
                stack.append(new_num)
            else:
                print(f'#{tc} error')
                return

T = int(input())
for tc in range(1, T + 1):
    quest = input().split() # ['5', '3', '*', '+', '.'] 알아서 리스트로
    forth(quest)

