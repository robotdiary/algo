n, m = map(int, input().split())
nm = n * m
arr = []  # 1차원으로 받았다리
for _ in range(n):
    arr += list(map(int, input().split()))

answer = 0
while sum(arr):
    cheese = []  # 녹일 치즈
    stack = [0]
    visited = [0] * nm
    visited[0] = 1
    while stack:
        current = stack.pop()
        for di in (1, -1, m, -m):  # 우, 좌, 하, 상
            ni = current + di
            if 0 <= ni < nm and arr[ni] == 0 and not visited[ni]:
                stack.append(ni)
                visited[ni] = 1
            elif 0 <= ni < nm and arr[ni] == 1:
                if visited[ni] == 0:
                    visited[ni] = 1
                elif visited[ni] == 1:
                    cheese.append(ni)
                    visited[ni] = 2

    # 겉에 나와있는 치즈들을 녹인다
    for melting in cheese:
        arr[melting] = 0
    answer += 1

print(answer)
