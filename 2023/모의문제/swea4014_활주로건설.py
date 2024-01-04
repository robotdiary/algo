'''
1차 : 40/50 틀림 -> 작아져서 사다리를 놨을 땐, cnt가 0으로 다시 시작하게 된다.
너무 하기 싫어서 못 할 것 같았는데 그냥 생각한 대로 짜니까 됐다.
슬퍼하지 말고 할 수 있는 걸 일단 구현하자
'''
def solve(lst):
    target = lst[0]  # 현재 숫자
    cnt = 1          # target이 반복된 횟수
    idx = 1          # 현재 인덱스
    while idx < N:
        if lst[idx] != target:
            # 한 칸 작아졌다
            if target - lst[idx] == 1:
                if lst[idx:idx + X] == [lst[idx]] * X:
                    target = lst[idx]
                    cnt = 0  # 1로 해서 틀림
                    idx = idx + X
                else:
                    return False
            # 한 칸 커졌다
            elif lst[idx] - target == 1:
                if cnt < X:
                    return False
                else:
                    target = lst[idx]
                    idx += 1
                    cnt = 1
            else:
                return False
        else:
            idx += 1
            cnt += 1
    return True


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    zip_arr = list(zip(*arr))

    answer = 0
    for i in range(N):
        if solve(arr[i]):
            answer += 1
        if solve(list(zip_arr[i])):
            answer += 1

    print(f'#{tc} {answer}')

