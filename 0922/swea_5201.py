# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split()) # 컨테이너, 트럭
    wi = list(map(int, input().split())) # 화물 무게
    ti = list(map(int, input().split())) # 트럭 용량
    answer = 0 # 옮긴 화물의 총 합
    wi.sort()
    ti.sort()
    for i in range(len(ti)):
        truck = ti.pop()
        while wi:
            container = wi.pop()
            if container <= truck:
                answer += container
                break
    print(f'#{tc} {answer}')

