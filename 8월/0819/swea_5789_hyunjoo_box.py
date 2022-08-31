# 5789. 현주의 상자 바꾸기 (D3)
T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split()) # n개의 상자, q회 동안 숫자 변경
    boxes = [0] * n
    for change in range(1, q+1):
        l, r = map(int, input().split())
        boxes[l-1:r] = [change] * (r - l + 1)
    print(f'#{tc}', *boxes)
