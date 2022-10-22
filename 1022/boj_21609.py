# boj 20609 상어중학교 (G2)
def select():
    global answer
    selected_block_group = [0, 0, [0]]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                block_num = arr[i][j]  # 일반 블럭 번호
                rainbow_nums = 0  # 무지개 블럭 개수
                block_rc = (0, 0)  # 기준 블럭 행과 열
                stack = [(i, j)]
                visited = set()
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        if 0 <= cr + dr < n and 0 <= cc + dc < n and (cr + dr, cc + dc) not in visited:
                            if arr[cr + dr][cc + dc] == 0:
                                stack.append((cr + dr, cc + dc))
                                visited.add((cr + dr, cc + dc))
                                rainbow_nums += 1
                            elif arr[cr + dr][cc + dc] == block_num:
                                stack.append((cr + dr, cc + dc))
                                visited.add((cr + dr, cc + dc))
                                if cr + dr > block_rc[0] and cc + dc > block_rc[1]:
                                    block_rc = (cr + dr, cc + dc)

                if len(visited) >= 2 and len(visited) > len(selected_block_group[2]):
                    selected_block_group = [rainbow_nums, block_rc, visited]
                elif len(visited) >= 2 and len(visited) == len(selected_block_group):
                    if rainbow_nums == selected_block_group[0]:
                        if block_rc[0] == selected_block_group[1][0]:
                            if block_rc[1] > selected_block_group[1][1]:
                                selected_block_group = [rainbow_nums, block_rc, visited]
                        elif block_rc[0] > selected_block_group[1][0]:
                            selected_block_group = [rainbow_nums, block_rc, visited]
                    elif rainbow_nums > selected_block_group[0]:
                        selected_block_group = [rainbow_nums, block_rc, visited]
    answer += len(selected_block_group[2]) ** 2
    return selected_block_group[2]


def pop_block(x):
    for i in x:
        arr[i[0]][i[1]] = 8

def gravity():
    print(arr)
    for i in range(n-2, -1, -1):
        for j in range(n):
            if arr[i][j] not in {-1, 8}:
                cr, cc = i, j
                while cr+1 < n and arr[cr+1][cc] == 8:
                    arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                    cr += 1
    return



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# while select():
pop_block(select())
gravity()
print(arr)

