T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 리스트 컴프리핸션 > for, append로 길게 쓰는 대신\

    # 원래 좋은 위치는 T와 for 사이(2번째 줄) 모든 tc가 쓰니까
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1] # 행과 열로 네가지 방향을 설정 # 두 배 하면 두 칸씩 감

    answer = 0
    # 일단 모든 애들을 한 번씩 돌아야지
    for r in range(N):# 행
        for c in range(N): # 열
            for i in range(4): # 좌, 우, 위, 아래 확인
                nr = r + dr[i]
                nc = c + dc[i] # 행과 열 구분 주의!
                # 가능한 범위면 해라 vs 범위 밖이면 하지 마라 다 가능
                if 0 <= nr < N and 0 <= nc < N:
                    answer += abs(arr[r][c] - arr[nr][nc])
    print(answer)