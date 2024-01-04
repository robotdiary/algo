from collections import defaultdict
R, C, K = map(int, input().split())
R -= 1
C -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

answer = 0
for tc in range(101):
    r_cnt = len(arr)
    c_cnt = len(arr[0])
    if R < r_cnt and C < c_cnt and arr[R][C] == K:
        print(tc)
        break
    # R연산
    new_arr = []
    if r_cnt >= c_cnt:
        mx = 0
        for lst in range(r_cnt):
            cnt = defaultdict(int)
            for i in arr[lst]:
                cnt[i] += 1
            need_sort = []
            for key, value in cnt.items():
                if value and key:
                    need_sort.append((value, key))
            need_sort.sort()
            result = []
            # 50개만 넣자
            idx = 0
            while idx < 50 and idx < len(need_sort):
                result.append(need_sort[idx][1])
                result.append(need_sort[idx][0])
                idx += 1
            new_arr.append(result)
            mx = max(mx, len(result))
        for r in range(r_cnt):
            while len(new_arr[r]) < mx:
                new_arr[r].append(0)
        arr = new_arr
        # print(arr)
    else:
        mx = 0
        for lst in range(c_cnt):
            cnt = defaultdict(int)
            for i in range(r_cnt):
                cnt[arr[i][lst]] += 1
            need_sort = []
            for key, value in cnt.items():
                if value and key:
                    need_sort.append((value, key))
            need_sort.sort()
            result = []
            # 50개만 넣자
            idx = 0
            while idx < 50 and idx < len(need_sort):
                result.append(need_sort[idx][1])
                result.append(need_sort[idx][0])
                idx += 1
            # print(result)
            new_arr.append(result)
            mx = max(mx, len(result))
        for r in range(c_cnt):
            while len(new_arr[r]) < mx:
                new_arr[r].append(0)
        # print(new_arr)
        # print(c_cnt)
        replace_arr = [[0] * c_cnt for _ in range(mx)]
        for i in range(mx):
            for j in range(c_cnt):
                replace_arr[i][j] = new_arr[j][i]
        arr = replace_arr

else:
    print(-1)