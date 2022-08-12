word = input()
alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for croa in alpa:
    if croa in word:
        word = word.replace(croa, '1')
for char in word:
    if char != '1':
        word = word.replace(char, '1')
count = 0
for i in word:
    count += int(i)
print(count)
