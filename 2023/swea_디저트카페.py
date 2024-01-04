
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = -1
    left , right = (n - 1) // 2, (n - 1) // 2 - 2
    while left and right:
        for i in range(0, n - 1 - left):
            for j in range(left, n - 1 - left):
                dessert = set()
                for k in range(left):
                    print(i + k, j + k)
                    print(i + left + k, j - left + k)
                for k in range(right):
                    print(i + 1 + k, j - 1 - k)
                    print(i + right + 1 + k, j + right - 1 - k)

                    # dessert.add(arr[i + k][j + k])
        if right != 1:
            right -= 1
        else:
            left -= 1
            right = (n - 1) // 2 - 2