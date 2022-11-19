# 숫자카드 2
from collections import defaultdict
from collections import Counter

N = int(input())
my_card_dict = Counter(list(map(int, input().split())))
N = int(input())
answer = []
for num in list(map(int, input().split())):
    answer.append(my_card_dict[num])
print(*answer)