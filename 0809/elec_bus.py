T = int(input())
for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    charging = list(map(int, input().split()))
    bus = 0  # 버스의 현재 위치
    bus_charging = 0  # 버스 충전 횟수
    # 버스 정류소를 충전기 유무 0, 1로 표현
    buses = [0] * (n + 1)  # 0번 정류장까지 포함
    for i in charging:
        buses[i] = 1

    # k칸 안에 충전소가 있으면 버스의 위치를 옮기고 충전횟수 늘리고 컨티뉴
    while bus < (n - k):  # n-k에서는 바로 종착점까지 갈 수 있으니까 버스가 n-k를 넘기 전까지 반복

        charging_tf = 0  # 이 턴 안에 충전을 했는지 안 했는지 체크
        # k 이하로 버스 이동시키기
        for j in range(k, 0, -1):  # 더 먼 데 정류장이 있으면 거기로 가야함
            # 충전소가 아닐 때
            if buses[bus + j] == 0:  # 정류소 중 버스가 갈 곳에 충전기가 있으면 > 없으면 continue를 해야하네
                continue  # 마지막까지 다 돌고 나면 그냥 빠져나간다.
            # 충전소일 때
            else:
                bus += j
                bus_charging += 1
                charging_tf = 1
                break  # for문을 나가는 break / while문 조건을 확인하고 다시 반복하게 된다.

        # 충전이 안 됐거나, while문 조건을 벗어나면 while문 중단
        if charging_tf == 0:
            break
    # 충전소가 없었다면
    if charging_tf == 0:
        print(f'#{tc} 0')
    # 끝까지 왔다면
    else:
        print(f'#{tc} {bus_charging}')