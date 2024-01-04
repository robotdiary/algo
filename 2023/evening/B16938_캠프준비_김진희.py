def 백준아도와줄게():
    global answer
    for i in range(1 << n):
        quest = []
        for j in range(n):
            if i & (1 << j):
                quest.append(dif[j])
        if len(quest) >= 2 and l <= sum(quest) <= r and max(quest) - min(quest) >= x:
            answer += 1


n, l, r, x = map(int, input().split())
dif = list(map(int, input().split()))
answer = 0
백준아도와줄게()
print(answer)