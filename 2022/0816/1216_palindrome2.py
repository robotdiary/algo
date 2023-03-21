def palindromn(matrix):
    maxcnt = 0
    for i in range(100):
        for j in range(99):
            for z in range(99, j, -1):
                count = 0
                if matrix[i][j] == matrix[i][z]:
                    count += 1
                    left = j + 1
                    right = z - 1
                    while right > left:
                        if matrix[i][left] == matrix[i][right]:
                            count += 1
                            if right - left == 2:
                                count = count * 2 + 1
                                if count > maxcnt:
                                    maxcnt = count
                                break
                            elif right - left == 1:
                                count = count * 2
                                if count > maxcnt:
                                    maxcnt = count
                                break
                            left += 1
                            right -= 1
                        else:
                            break
    return maxcnt

for T in range(1, 11):
    tc = int(input())
    matrix = [[0]*100 for _ in range(100)]
    for i in range(100):
        char = input()
        for j in range(100):
            matrix[i][j] = char[j]
    result = palindromn(matrix)
    matrix2 = list(map(list, zip(*matrix)))
    if palindromn(matrix2) > result:
        result = palindromn(matrix2)
    print(f'#{tc} {result}')