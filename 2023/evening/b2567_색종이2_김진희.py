# 0에서 1로 변할때, 1에서 0으로 변할때가 곧 가장자리라는 생각!
# 맨 끝이 종이(1)인채로 끝나도 셀 수 있도록 0인 가장자리를 붙여준다 -> 101개의 0
arr = [[0]*101 for _ in range(101)]

# 종이로 배열 채우기
for tc in range(int(input())):
    c, r = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[r + i][c + j] = 1

# 배열 돌면서 0->1 or 1->0일 때 answer를 1 올려준다
answer = 0
for i in range(101):
    r_check = 0  # 이전에 0이었는지 1이었는지 기록
    c_check = 0
    for j in range(101):
        # 가로 방향 확인
        if not r_check and arr[i][j]:
            answer += 1
            r_check = 1
        elif r_check and not arr[i][j]:
            answer += 1
            r_check = 0
        # 세로 방향 확인
        if not c_check and arr[j][i]:
            answer += 1
            c_check = 1
        elif c_check and not arr[j][i]:
            answer += 1
            c_check = 0
print(answer)

