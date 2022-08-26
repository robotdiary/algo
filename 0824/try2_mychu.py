# 마이쮸
from collections import deque

line = deque([[1, 1]])
mychu = 20
while mychu > 0:
    man = line.popleft()
    mychu -= man[1]
    if mychu < 1:
        print(man[0])
        break
    man[1] += 1
    line.append(man)
    line.append([man[0] + 1, 1])