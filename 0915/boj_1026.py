n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0
for i in range(n):
    answer += b.pop(b.index(max(b))) * a.pop(a.index(min(a)))

print(answer)
# print(b.pop(b.index(max(b))))
# print(a.pop(a.index(min(a))))