# 11315 오목
# [3]번 코드
def omok_check():
    for i in range(n):
        for j in range(n):
            for d in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                for check in range(5):
                    if 0 <= i+d[0]*check < n and 0 <= j+d[1]*check < n and arr[i+d[0]*check][j+d[1]*check] == 'o':
                        continue
                    else:
                        break
                else:
                    return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    print(f'#{tc} {omok_check()}')

# [2]번 코드
def omok_check():
    for i in range(n):
        for j in range(n):
            for check in range(5): # 1, 0
                if j+check < n and arr[i][j+check] == 'o':
                    continue
                else:
                    break
            else:
                return 'YES'
            for check in range(5):
                if j+check < n and arr[j+check][i] == 'o':
                    continue
                else:
                    break
            else:
                return 'YES'
            for check in range(5):
                if i+check < n and j+check < n and arr[i+check][j+check] == 'o':
                    continue
                else:
                    break
            else:
                return 'YES'
            for check in range(5): # 4, 0
                if i-check >= 0 and j + check <= n-1 and arr[i-check][j+check] == 'o':
                    continue
                else:
                    break
            else: return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    print(f'#{tc} {omok_check()}')

# [3]번 코드 : 보충교수님
def solve():
    # [1] 수평으로 오목체크
    for si in range(N):
        for sj in range(N - 5 + 1):  # 가능한 모든 시작위치
            for d in range(5):
                if arr[si][sj + d] != 'o':
                    break
            else:
                return 'YES'

    # [2] 수평으로 오목체크
    for sj in range(N):
        for si in range(N - 5 + 1):  # 가능한 모든 시작위치
            for d in range(5):
                if arr[si + d][sj] != 'o':
                    break
            else:
                return 'YES'

    # [3] 우측하단 대각선 오목체크
    for si in range(N - 5 + 1):
        for sj in range(N - 5 + 1):  # 가능한 모든 시작위치
            for d in range(5):
                if arr[si + d][sj + d] != 'o':
                    break
            else:
                return 'YES'

    # [4] 우측상단 대각선 오목체크
    for si in range(4, N):
        for sj in range(N - 5 + 1):  # 가능한 모든 시작위치
            for d in range(5):
                if arr[si - d][sj + d] != 'o':
                    break
            else:
                return 'YES'

    # 위에서 리턴을 못했다면... 못 찾음
    return 'NO'


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    ans = solve()

    print(f"#{test_case} {ans}")