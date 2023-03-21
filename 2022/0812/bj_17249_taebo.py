taebo = input()
left = 0
right = 0
middle = taebo.find('0')
for i in taebo[:middle-2]:
    if i == '@':
        left += 1
for i in taebo[-1:middle+2:-1]:
    if i == '@':
        right += 1
print(left, right)