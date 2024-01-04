# 올바른것???
# 일단 중복 방문하지 않고
# 나이트가 움직일 수 있는 방향으로만 가고
# 36개의 칸을 모두 간다
# 처음칸으로 돌아올 수 있다
answer = 'Invalid'
visited = set()
cc, cr = input()
cc = ord(cc) - 65
cr = int(cr) - 1
visited.add((cr, cc))
first = (cr, cc)

for _ in range(35):
    c, r = input()
    c = ord(c) - 65
    r = int(r) - 1
    # 중복이냐
    if (r, c) in visited:
        break
    visited.add((r, c))

    # 갈 수 있는 방향이냐
    if (r, c) not in {(cr - 2, cc - 1), (cr - 2, cc + 1), (cr - 1, cc - 2), (cr - 1, cc + 2), (cr + 1, cc - 2), (cr + 1, cc + 2), (cr + 2, cc - 1), (cr + 2, cc + 1)}:
        break
    cr, cc = r, c
else:
    if first in {(cr - 2, cc - 1), (cr - 2, cc + 1), (cr - 1, cc - 2), (cr - 1, cc + 2), (cr + 1, cc - 2), (cr + 1, cc + 2), (cr + 2, cc - 1), (cr + 2, cc + 1)}:
        answer = 'Valid'

print(answer)