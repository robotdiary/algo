'''
네 꼭지점을 먼저 구해! 그리고 엔퀸의 대각선 비법으로 영역을 구분할 수 있다.
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = 99999
# [1] 네모 만들기
# [1-1] 맨 위 시작 꼭지점 설정
for i in range(N-2):
    for j in range(1, N-1):
        # [1-2] 오른 대각선 크기
        for k in range(1, N-1):
            for d in range(1, N-1):
                # 모든 꼭지점이 범위 안인지 확인
                if i + k + d < N and 0 <= j - k < j + d < N:
                    people = [0, 0, 0, 0, 0]
                    # [2] 부족별 인구수 세기
                    for dr in range(N):
                        for dc in range(N):
                            if dr < i+k and dc <= j and dr + dc < i + j:
                                people[0] += arr[dr][dc]
                                visited[dr][dc] = 1
                            elif dr <= i + d and dc > j and dr - dc < i - j:
                                people[1] += arr[dr][dc]
                                visited[dr][dc] = 2
                            elif dr >= i + k and dc < j - k + d and dr-dc > i - j + k + k:
                                people[2] += arr[dr][dc]
                                visited[dr][dc] = 3
                            elif dr > i + d and dc >= j - k + d and dr + dc > i + j + d + d:
                                people[3] += arr[dr][dc]
                                visited[dr][dc] = 4
                            else:
                                people[4] += arr[dr][dc]
                                visited[dr][dc] = 5
                    if max(people) - min(people) < answer:
                        print((i,j), (i+k, j-k), (i+d, j+d), (i+d+k, j - k + d))
                        print(*visited, sep='\n')
                        print()
                    answer = min(answer, (max(people) - min(people)))
print(answer)


