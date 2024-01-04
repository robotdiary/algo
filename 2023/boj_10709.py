# 기상캐스터
h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]

for i in range(h):
    pre = -1   # 표시할 예측값
    cloud = 0  # 이전에 구름이 있었는지 표시
    for j in range(w):
        if arr[i][j] == 'c':  # 구름이 등장하면 cloud를 1로 바꿔 줌
            cloud = 1
            pre = -1          # 등장한 순간부터 1씩 증가해야하는 pre 초기화
        if cloud:             # 구름이 있었으면 pre를 1씩 증가시키면서 써줄거고요
            pre += 1
        arr[i][j] = pre       # 구름이 없었다면 계속 -1일 겁니다

for answer in arr:
    print(*answer)
