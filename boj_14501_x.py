# 퇴사
def work(day):
    answer


N = int(input())  # 1-15
schedule = []
for i in range(N):
    schedule.append((map(int, input().split())))
answer = 0
for i, j in schedule:
    work(i, j)
print(answer)