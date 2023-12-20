from collections import defaultdict
R, C, K = map(int, input().split())
R -= 1
C -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

for tc in range(100):
    N, M = len(arr), len(arr[0])

    if R < N and C < M and arr[R][C] == K:
        print(tc)
        break

    # [1-1] 행의 개수 > 열
    if N >= M:
        new_arr = [[] for _ in range(N)]
        mx = 0
        # [2] 모든 행에 대하여 정렬 (출현빈도 적은, 숫자 작은 순) 숫자, 빈도
        for i in range(N):
            # 숫자 세기
            cnt_dict = defaultdict(int)
            for j in range(M):
                if arr[i][j]:
                    cnt_dict[arr[i][j]] += 1
            # 출현 빈도 순으로 정렬
            cnt_lst = []
            for key, v in cnt_dict.items():
                cnt_lst.append((v, key))
            cnt_lst.sort()
            mx = max(mx, min(100, len(cnt_lst) * 2))
            # 숫자, 빈도 순으로 100개 넣기
            for cnt, num in cnt_lst[:50]:
                new_arr[i].append(num)
                new_arr[i].append(cnt)
        # 길이 맞추기
        for i in range(N):
            new_arr[i] += [0] * (mx - len(new_arr[i]))
        arr = new_arr

    # [1-2] 열 > 행
    else:
        new_arr = [[] for _ in range(M)]
        mx = 0
        # [2] 모든 열에 대하여 정렬 (출현빈도 적은, 숫자 작은 순) 숫자, 빈도
        for j in range(M):
            # 숫자 세기
            cnt_dict = defaultdict(int)
            for i in range(N):
                if arr[i][j]:
                    cnt_dict[arr[i][j]] += 1
            # 출현 빈도 순으로 정렬
            cnt_lst = []
            for key, v in cnt_dict.items():
                cnt_lst.append((v, key))
            cnt_lst.sort()
            mx = max(mx, min(100, len(cnt_lst) * 2))
            # 숫자, 빈도 순으로 100개 넣기
            for cnt, num in cnt_lst[:50]:
                new_arr[j].append(num)
                new_arr[j].append(cnt)
        # 길이 맞추기
        for i in range(M):
            new_arr[i] += [0] * (mx - len(new_arr[i]))

        table = [[0] * M for _ in range(mx)]
        for i in range(mx):
            for j in range(M):
                table[i][j] = new_arr[j][i]
        arr = table

else:
    if R < len(arr) and C < len(arr[0]) and arr[R][C] == K:
        print(100)
    else:
        print(-1)