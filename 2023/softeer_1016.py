n = int(input())  # 참가자 수

a_cup = list(map(int, input().split()))
b_cup = list(map(int, input().split()))
c_cup = list(map(int, input().split()))

a_rank = sorted(a_cup, reverse=True)
b_rank = sorted(b_cup, reverse=True)
c_rank = sorted(c_cup, reverse=True)

final_cup = [0] * n # 점수 합계
for i in range(n):
    final_cup[i] = a_cup[i]+b_cup[i]+c_cup[i]
final_rank = sorted(final_cup)

a_answer = []
b_answer = []
c_answer = []
final_answer = []
for z in range(n):
    a_answer.append(a_rank.index(a_cup[z]) + 1)
    b_answer.append(b_rank.index(b_cup[z]) + 1)
    c_answer.append(c_rank.index(c_cup[z]) + 1)
    final_answer.append(final_rank.index(final_cup[z]) + 1)

print(*a_answer)
print(*b_answer)
print(*c_answer)
print(*final_answer)