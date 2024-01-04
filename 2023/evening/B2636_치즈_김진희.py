n, m = map(int, input().split())
nm = n * m
arr = []  # 1차원으로 받았다리
for _ in range(n):
    arr += list(map(int, input().split()))

answer = 0
cheese = []  # 이번 턴에 녹일 치즈를 모아놓는다
# 1차원으로 만들어서 sum()을 쓸 수 있고, 치즈가 없어진 것을 바로 확인 가능!
while sum(arr):
    cheese = []  # 턴을 돌 때, 녹일 치즈 초기화
    stack = [0]
    visited = [0] * nm
    visited[0] = 1
    while stack:
        current = stack.pop()
        for di in (1, -1, m, -m):  # 우, 좌, 하, 상
            ni = current + di
            if 0 <= ni < nm and not visited[ni]:
                if arr[ni]:
                    cheese.append(ni)
                    visited[ni] = 1
                else:
                    stack.append(ni)
                    visited[ni] = 1

    # 겉에 나와있는 치즈들을 녹인다
    for melting in cheese:
        arr[melting] = 0
    answer += 1

print(answer)
print(len(cheese))
