# 5431 민석이의 과제 체크하기 (D3)
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    students = set(i for i in range(1, n+1))
    sub = set(map(int, input().split()))
    print(f'#{tc}', *sorted(list(students - sub)))


