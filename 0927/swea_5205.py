# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
def quick_sort(low, high):
    def partition(low, high):
        pivot = nums[high]
        left = low
        for right in range(low, high):
            if nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        nums[left], nums[high] = nums[high], nums[left]
        return left
    if low < high:
        pivot = partition(low, high)
        quick_sort(low, pivot-1)
        quick_sort(pivot+1, high)


for tc in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, len(nums)-1)
    print(f'#{tc} {nums[n//2]}')