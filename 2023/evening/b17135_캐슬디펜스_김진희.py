'''
제출 시 틀린 것
한 턴에 같은 적이 공격 당할 수 있음! 턴이 끝난 뒤에 사라지는 것
bfs의 길이 카운트 세는 부분
나중에 수정하려니까 꼬여서 여기저기서 틀림 특히 bfs부분
누덕 누덕 기우지 말고 새로 다시 짜기 노력하자
푸는 중 실수
다 쓰고 문제랑 맞는지 다시 한 번 체크하기!
거리 문장도 놓쳤고, nr의 범위가 n까지가 아닌 0 <= nr < i, bfs인데 stack을 써버림
'''
from collections import deque


def comb(depth, start, lst):
    if depth == 3:
        bfs(lst)
        return
    for i in range(start, m):
        comb(depth + 1, i + 1, lst + [i])


def bfs(lst):
    global answer
    acc = 0
    enemy = set()
    for i in range(n, 0, -1):
        attacked = set()
        for idx in lst:
            q = deque([(i, idx)])
            visited = [[0] * m for _ in range(n)]
            distance = d
            while distance and q:
                for k in range(len(q)):
                    cr, cc = q.popleft()
                    for dr, dc in (0, -1), (-1, 0), (0, 1):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < i and 0 <= nc < m and visited[nr][nc] == 0:
                            if arr[nr][nc] == '1' and (nr, nc) not in enemy:
                                attacked.add((nr, nc))
                                q = 0
                                break
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                    if not q:
                        break
                else:
                    distance -= 1
        for ar, ac in attacked:
            enemy.add((ar, ac))
            acc += 1
    answer = max(answer, acc)


n, m, d = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]  # 문자열
answer = 0
comb(0, 0, [])
print(answer)