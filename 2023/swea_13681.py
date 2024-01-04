for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    zip_arr = list(zip(*arr))

    for i in range(9):
        if len(set(arr[i])) != 9 or len(set(zip_arr[i])) != 9:
            print(f'#{tc} 0')
            break
        check = set()
        for j in range(3):
            check.add(arr[i % 3 * 3][i // 3 * 3 + j])
            check.add(arr[i % 3 * 3 + 1][i // 3 * 3 + j])
            check.add(arr[i % 3 * 3 + 2][i // 3 * 3 + j])
        if len(check) != 9:
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')