# 마그네틱
for tc in range(1, 11):
    n = int(input())  # 테이블 크기 항상 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    # 세로로 확인하면서 1과 2가 세트로 이어서 나오면 answer를 1증가시킬 것
    for j in range(100):
        check = 0  # 1이 나왔는지 체크해줄 변수
        for i in range(100):
            if arr[i][j] == 1:              # 1이 나오면 일단 체크해둔다
                check = 1
            elif arr[i][j] == 2 and check:  # 2가 나왔을 때, 1이 체크 되어있으면 한 쌍이다
                answer += 1
                check = 0                   # 한 쌍을 판별했으므로 다시 체크 초기화

    print(f'#{tc} {answer}')

