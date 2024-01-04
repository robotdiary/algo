from collections import deque
import sys

n = sys.stdin.readline().rstrip()  # 문자열 : 원하는 채널
m = int(sys.stdin.readline().rstrip())  # 고장난 버튼 개수
if int(n) == 100:  # 원하는 채널이 100이면 그대로
    if m:
        throw = sys.stdin.readline().rstrip()
    print(0)
else:  # 원하는 채널이 100이 아닐 때
    if m:  # 고장난 버튼이 있을 때
        broken = sys.stdin.readline().rstrip().split()  # 고장난 버튼 리스트
        q = deque([n])  # 문자열로 넣기
        visited = {int(n)}  # 숫자로 넣기
        # 모든 채널이 고장났을 때
        if m == 10:
            print(abs(int(n) - 100))
            q = False
        while q:
            str_btn = q.popleft()  # 채널 숫자 문자열
            # 방향키 조작이 더 빠른 경우 방향키로 이동하기
            if str_btn == "100":
                print(abs(int(n) - int(str_btn)))
                break
            for char_btn in str_btn:  # 채널 숫자를 하나씩 돌면서
                if char_btn in broken:
                    if int(str_btn) - 1 not in visited and int(str_btn) - 1 >= 0:
                        visited.add(int(str_btn) - 1)
                        q.append(str(int(str_btn) - 1))
                    if int(str_btn) + 1 not in visited:
                        visited.add(int(str_btn) + 1)
                        q.append(str(int(str_btn) + 1))
                    break
            else:
                print(min(len(str_btn) + abs(int(n) - int(str_btn)), abs(int(n) - 100)))
                break

    else:  # 고장난 버튼이 없을 때
        print(min(len(n), abs(int(n) - 100)))
