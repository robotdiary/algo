def magic_star(lst, depth):
    # 숫자 모이는 대로 한 줄씩 확인해서 26이 안 되면 바로 버릴게요
    if depth == 12:
        if lst[4] + lst[6] + lst[9] + lst[11] != 282 or lst[1] + lst[8] + lst[5] + lst[11] != 282:
            return
        print_star(lst)  # 모든 숫자가 26 통과해서 도착 했을 때만 프린트
        return
    elif depth == 5:
        if sum(lst[1:5]) != 282:
            return
    elif depth == 8:
        if lst[0] + lst[2] + lst[5] + lst[7] != 282:
            return
    elif depth == 11:
        if sum(lst[7:11]) != 282 and lst[0] + lst[3] + lst[6] + lst[10] != 282:
            return

    if star[depth]:  # 존재하는 애는 걔로 넣고
        magic_star(lst + [star[depth]], depth + 1)
    else:            # x인 애만 이것 저것 넣어보면서 들어감
        for i in range(65, 77):
            if not visited[i-64]:
                visited[i-64] = 1
                magic_star(lst + [i], depth + 1)
                visited[i-64] = 0


def print_star(lst):
    print(f'....{chr(lst[0])}....')
    print(f'.{chr(lst[1])}.{chr(lst[2])}.{chr(lst[3])}.{chr(lst[4])}.')
    print(f'..{chr(lst[5])}...{chr(lst[6])}..')
    print(f'.{chr(lst[7])}.{chr(lst[8])}.{chr(lst[9])}.{chr(lst[10])}.')
    print(f'....{chr(lst[11])}....')
    exit(0)


star = []  # 일단 .은 버리고 열두개의 숫자와 x만 모으자
visited = [0] * 13
for _ in range(5):
    for char in input():
        if 77 > ord(char) > 64:          # 알파벳이면 숫자로 넣고
            star.append(ord(char))
            visited[ord(char) - 64] = 1  # 이미 있다고 체크해두고
        elif ord(char) > 64:             # x면 0으로 넣을게요
            star.append(0)
magic_star([], 0)
