import copy


def solution(rc, operations):
    answer = rc
    now_command = -1
    command_stack = 0
    for command in operations:
        if command == "ShiftRow":
            # shiftrow로 되어 있을 때
            if now_command:
                command_stack += 1
            # shitfrow가 아닐 때
            else:
                answer = Rotate(answer, command_stack)
                now_command = 1
                command_stack = 1
        else:
            # rotate로 되어 있을 때
            if not now_command:
                command_stack += 1
            # rotate가 아닐 때
            else:
                answer = ShiftRow(answer, command_stack)
                now_command = 0
                command_stack = 1
    return answer


def ShiftRow(array, cs):
    ans = []
    for i in range(len(array)):
        ans.append(array[(len(array) - 2 + cs + i) % len(array)])
    return ans


def Rotate(array, cs):
    ans = copy.deepcopy(array)

    # 도는 방향
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0

    # 첫째칸은 미리 채워둬볼게
    ans[0][0] = array[1][0]

    # 채워질 ans의 자리
    nr, nc = 0, 0

    while d < 4:
        if 0 <= nr + direction[d][0] < len(array) and 0 <= nc + direction[d][1] < len(array[0]):
            ans[nr + direction[d][0]][nc + direction[d][1]] = array[nr][nc]
            nr, nc = nr + direction[d][0], nc + direction[d][1]
        else:
            d += 1
    return ans


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))