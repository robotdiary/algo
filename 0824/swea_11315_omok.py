# 11315 오목
def omok_check():
    for i in range(n):
        for j in range(n):
            for check in range(5):
                if j+check < (n-4) and [i][j+check] == 'o':
                    continue
                else:
                    break
            else:
                return 1
            for check in range(5):
                if j+check < n-4 and [j+check][i] == 'o':
                    continue
                else:
                    break
            else:
                return 1
            for check in range(5):
                if i+check < n-4 and j+check < n-4 and [i+check][j+check] == 'o':
                    continue
                else:
                    break
            else:
                return 1
            for check in range(5):
                if



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]