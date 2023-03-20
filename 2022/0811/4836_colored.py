T = int(input())
for tc in range(1, T+1):
    n = int(input())
    color = [list(map(int, input().split())) for _ in range(n)]
# 빨간 박스와 파란 박스를 칠할 10칸짜리 빈 박스 두 개
    block1 = [[0]*10 for _ in range(10)]
    block2 = [[0]*10 for _ in range(10)]
    count = 0
# color에서 한 줄씩 가져와서 맨 끝이 1이면 1번 박스에 2면 2번 박스에 칠한다
    for line in color:
        for i in range(line[0], line[2]+1): # 왼쪽 위 칸부터 왼쪽 아래 칸까지 내려갈건데
            for j in range(line[1], line[3]+1): # 왼쪽 숫자부터 오른쪽 숫자까지 칠하고 가
                if line[-1] == 1: # 빨강색은 여기 칠하고
                    block1[i][j] = 1
                else: # 파랑색이면 여기 칠해
                    block2[i][j] = 1
# 다 칠한 박스들을 가지고 둘 다 1로 칠해져 있는지 확인
    for i in range(10):
        for j in range(10):
            if block1[i][j] == 1 and block2[i][j] == 1: # block1[i][j] == block2[i][j] == 1 하면 안 된다.
                count += 1
    print(f'#{tc} {count}')