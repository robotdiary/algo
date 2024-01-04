def bubble_sort(target):
    # 모든 원소에 대하여
    for i in range(n-1):
        # 뒤의 애들과 비교하면서 자리를 찾을 것
        for j in range(n-1-i):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    return target


def quick_sort(target, start, end):
    if start >= end:
        return

    pivot = start  # 맨 앞 녀석이 피봇
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 녀석 찾기
        while left <= end and target[left] <= target[pivot]:
            left += 1
        # 피봇보다 작은 녀석 찾기
        while right > start and target[right] >= target[pivot]:
            right -= 1

        # 엇갈렸으면 작은 녀석과 피봇 교체
        if left > right:
            target[right], target[pivot] = target[pivot], target[right]
        # 아니면 작은 녀석과 큰 녀석 교체
        else:
            target[left], target[right] = target[right], target[left]
    # 좌우로 분할해서 각각 다시 정렬
    quick_sort(target, start, right - 1)
    quick_sort(target, right + 1, end)

    return target


for tc in range(1, int(input()) + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc}', *bubble_sort(lst))
    # print(f'#{tc}', *quick_sort(lst, 0, len(lst) - 1))