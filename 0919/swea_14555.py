# 14555. 공과 잡초 D3
T = int(input())
for tc in range(1, T + 1):
    # 문자열은 수정이 불가하므로 리스트로 받음
    field = list(input())
    balls = 0
    # 공이 겹치지 않으니까 공의 짝을 모두 맞춰준다
    for i in range(len(field)):
        if field[i] == '(':
            field[i+1] = ')'
        elif field[i] == ')':
            field[i-1] = '('
    # 공을 센다
    for i in field:
        if i == '(':
            balls += 1

    print(f'#{tc} {balls}')