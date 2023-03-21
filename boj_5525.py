# IOIOI
n = int(input())
m = int(input())
s = input()
pattern = "I"+"OI"*n
answer = 0
for i in range(m-(n*2)):
    if s[i:i+(2*n)+1] == pattern:
        answer += 1
print(answer)