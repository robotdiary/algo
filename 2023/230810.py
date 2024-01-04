def merge_sort(x):
    if len(x) < 2:
        return x
    left = merge_sort(x[:len(x) // 2])
    right = merge_sort(x[len(x) // 2:])
    sorted_lst = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_lst.append(left[l])
            l += 1
        else:
            sorted_lst.append(right[r])
            r += 1
    return sorted_lst + left[l:] + right[r:]


def binary_search(x):
    l = 0
    r = n - 1
    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == x:
            return 1
        elif lst[middle] < x:
            l = middle + 1
        else:
            r = middle - 1
    return 0


n = int(input())
lst = list(map(int, input().split()))
lst = merge_sort(lst)
m = int(input())
find = list(map(int, input().split()))
for target in find:
    print(binary_search(target))