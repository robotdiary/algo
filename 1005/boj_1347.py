# boj 1347 미로만들기 S3
n = int(input())
arr = [['#'] * (n * 2 + 1) for _ in range(n * 2 + 1)]  # 가운데에서 시작했을 때, 최대
info = input()
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하, 우, 상, 좌
r, c = n, n  # 현재 위치 가운데
arr[n][n] = '.'  # 현재 위치를 '.'으로
next = 0  # 회전한 후 나아갈 방향

# [1] 이동 데이터를 확인하면서 배열에 지도 쓰기
for i in info:
    # [2] F면 앞을 '.'로
    if i == 'F':
        arr[r+d[next % 4][0]][c+d[next % 4][1]] = '.'
        r += d[next % 4][0]
        c += d[next % 4][1]
    # [3] L이면 d에서 인덱스 + 1 한 방향임
    elif i == 'L':
        next += 1
    # [4] R이면 d에서 인덱스 + 1 한 방향임
    else:
        next -= 1

# [5] 전체 배열 중에 답이 되는 지도 부분만 추출
sr = set()  # 열의 인덱스
sc, ec = n*3, 0  # 행의 인덱스
for i in range(n * 2 + 1):
    # [6] 열의 인덱스 : '.'이 포함된 행을 모두 set(sr)에 추가
    if '.' in arr[i]:
        sr.add(i)
        # [7] 행의 인덱스 : 가장 앞과 뒤의 '.'을 찾기
        if arr[i].index('.') < sc:  # index 함수를 쓰면 가장 앞에 있는 '.'의 인덱스 반환
            sc = arr[i].index('.')
        for j in range(len(arr[i])):  # j를 돌면서 가장 큰 j만 저장
            if arr[i][j] == '.' and j > ec:
                ec = j
# [8] set(sr)의 최소값~최대값이 출력할 프린트의 줄
for i in range(max(sr) - min(sr) + 1):
    # [9] arr[i] 배열에서 sr~ec의 인덱스를 빈칸 없이 출력
    print(''.join(arr[min(sr)+i][sc:ec+1]))