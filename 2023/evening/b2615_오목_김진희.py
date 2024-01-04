# 오목
# 1 검 / 2 흰
# 좌하강 시 x- y+ 인거 리턴할 때 잘못 썼고!!
# 범위도 틀렸고, 16까지 가능한데 15인줄
# 오목의 전 후 이어지지 않는지 다 봐야하는데 후만 봤고
# 인덱스 에러 y+5를 y+6이라고 했군

def omok_game(me, x, y):
    # 가로 검사
    if y < 16 and arr[x][y:y+5] == [me] * 5 and arr[x][y+5] != me and arr[x][y - 1] != me:
        return me, x, y
    # 세로 검사
    if x < 16 and arr[x+5][y] != me and arr[x-1][y] != me:
        for check in range(1, 5):
            if arr[x + check][y] != me:
                break
        else:
            return me, x, y
    # 오른쪽 대각선 아래로
    if y < 16 and x < 16 and arr[x+5][y+5] != me and arr[x-1][y-1] != me:
        for check in range(1, 5):
            if arr[x + check][y + check] != me:
                break
        else:
            return me, x, y
    # 왼쪽 대각선 아래로
    if 4 < y and x < 16 and arr[x + 5][y - 5] != me and arr[x-1][y+1] != me:
        for check in range(1, 5):
            if arr[x + check][y - check] != me:
                break
        else:
            return me, x + 4, y - 4
    return 0, 0, 0


arr = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21]
winner, r, c = 0, 0, 0
for i in range(1, 20):
    for j in range(1, 20):
        if arr[i][j]:
            winner, r, c = omok_game(arr[i][j], i, j)
            if winner:
                print(winner)
                print(r, c)
                exit(0)
print(0)
