'''
총 풀이 시간 : 57분
20분 : 첫 구현에 tc 통과 못함
37분 : 잘못 구현한 부분 찾아서 테케 통과 완료
----------------------------------------
잘못 푼 부분
- 진행 방향부터 청소가 아니라, 90도 옆부터 먼저 선택
중간에 발견한 것
- 초기 방향 설정을 안 함(시작 방향과 내가 설정한 방향이 다름)
고민한 부분 : 방문을 nr nc일 때 바로 찍어도 되나???  --> 안 되는데 왜 안 되는지 모르겠다
'''
n, m = map(int, input().split())
cr, cc, d = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]  # 문자열
di = (0, 1, 0, -1)
dj = (-1, 0, 1, 0)
answer = 1

# 초기 방향 잘못 설정
dir_dic = {0: 3, 1: 2, 2: 1, 3: 0}
d = dir_dic[d]
# d % 4 잊지말자
while True:
    if arr[cr][cc] == '0':
        answer += 1
        arr[cr][cc] = 0  # 청소함

    for direction in range(1, 5):  # 일단 돌고 시작하는구나
        nr, nc = cr + di[(d + direction) % 4], cc + dj[(d + direction) % 4]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == '0':
            d += direction
            cr, cc = nr, nc
            # answer += 1
            # arr[cr][cc] = 0  # 청소함
            break
    else:
        nr, nc = cr + di[(d + 2) % 4], cc + dj[(d + 2) % 4]
        if not 0 <= nr < n or not 0 <= nc < m or arr[nr][nc] == '1':
            break
        else:
            cr, cc = nr, nc
            # if arr[cr][cc] == '0':
            #     answer += 1
            #     arr[cr][cc] = 0

print(answer)