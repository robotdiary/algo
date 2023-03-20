# D 오락실에 간 총총이
N = int(input())
arr = [list(input()) for _ in range(N)]
lt = [0, 0]
rt = [0, 0]
lb = [0, 0]
rb = [0, 0]
for i in range(N):
    if 'G' in arr[i]:
        for j in range(N):
            if arr[i][j] == 'G':
                lt[0] = max(lt[0], i)
                lt[1] = max(lt[1], j)
                rt[0] = max(rt[0], i)
                rt[1] = max(rt[1], ((N-1)-j))
                lb[0] = max(lb[0], ((N-1)-i))
                lb[1] = max(lb[1], j)
                rb[0] = max(rb[0], ((N-1)-i))
                rb[1] = max(rb[1], ((N-1)-j))
answer = min(sum(lt), sum(rt), sum(lb), sum(rb))
print(answer)