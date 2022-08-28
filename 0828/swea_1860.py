# 1860 진기의 최고급 붕어빵 (D3) 10:47 - 12:19
# while문으로 계속 실패 했는데 for문으론 성공 ㅠㅠㅠ 왜 안되는지 모르겟음
T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split()) #  n사람, m초, k개
    people = list(map(int, input().split())) # 도착 초
    a = sorted(people) # 검색용
    bread = 0
    second = 1
    result = 'Possible'
    for j in range(max(people)): # 손님이 올 때까지 영업
        # [0] 0초에 사람이 오면 실패
        if 0 in a:
            result = 'Impossible'
            break
        # [1] 시간이 되면 빵 추가
        if second % m == 0:
            bread += k
        # [2] 손님이 있고 빵이 없으면 실패
        if second in a and not bread:
            result = 'Impossible'
            break
        # [3] 손님이 있고 빵이 있으면 손님만큼 빵 빼고 빵 부족시 실패
        elif second in a and bread:
            person = people.count(second)
            bread -= person
            if bread < 0:
                result = 'Impossible'
                break
            if person > 1:
                for i in range(person):
                    people.remove(second)
            else:
                people.remove(second)
        # [4] 손님 다 보냈으면 끝
        if people == 0:
            break
        # [5] 시간이 흐른다
        second += 1
        # [6] 손님을 무사히 다 보냈으면 성공
    print(f'#{tc} {result}')