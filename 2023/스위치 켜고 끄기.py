n = int(input())
switches = [0] + list(map(int, input().split()))
s = int(input())
for _ in range(s):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number, n + 1, number):
            switches[i] ^= 1
    else:
        switches[number] ^= 1
        left = number - 1
        right = number + 1
        while 0 < left and right <= n and switches[left] == switches[right]:
            switches[left] ^= 1
            switches[right] ^= 1
            left -= 1
            right += 1

for i in range(1, n + 1, 20):
    print(*switches[i:i + 20])