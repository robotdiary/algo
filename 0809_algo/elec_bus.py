T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    charging = list(map(int, input().split()))
    buses = [0] * (n + 4) # 0번 정류장까지 포함
    bus = 0 # 버스의 위치
    bus_charging = 0 # 버스 충전 횟수
    # 버스 정류소를 충전기 유무 0, 1로 표현
    for i in charging:
        buses[i] = 1
    # k칸 안에 충전소가 있으면 버스의 위치를 옮기고 충전횟수 늘리고 컨티뉴
    while bus < (n-k):
        for j in range(k, 0, -1): # 더 먼 데 정류장이 있으면 거기로 가야지
            if buses[bus+j]: # 정류소 중 버스가 갈 곳에 충전기가 있으면
                bus += j
                bus_charging += 1
                # if bus > (n-k): # 클 수도 있찌
                #     print(f'#{tc} {bus_charging}')
                break
    # 충전기가 없으면 0을 출력 근데 끝까지 간 것도 생각해야해
        else:
            print(f'#{tc} 0')
            break