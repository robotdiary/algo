def quick_sort(left, right):
    if left < right:  # 종료 조건
        pivot = a[right]
        r = left      # 0이 아니라 리스트 맨 앞
        for i in range(left, right):
            if a[i] < pivot:
                a[r], a[i] = a[i], a[r]
                r += 1
        a[r], a[right] = a[right], a[r]

        quick_sort(left, r - 1)  # :r이 아니니까 r-1
        quick_sort(r + 1, right)


def merge_sort(lst):
    global answer

    if len(lst) == 1:
        return lst

    sorted_list = []
    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])
    if right[-1] < left[-1]:
        answer += 1
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1

    return sorted_list + left[l:] + right[r:]


for tc in range(1, int(input()) + 1):
    n = int(input())
    a = list(map(int, input().split()))
    # quick_sort(0, n - 1)  # 인덱스니까 n - 1
    answer = 0

    print(merge_sort(a)[n//2], answer)