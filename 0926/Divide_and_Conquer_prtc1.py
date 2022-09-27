# 연습 문제 1
# [1] 퀵정렬 - 로무토(끝피봇)
def lomuto(low, high):
    def partition(low, high):  # L위치 뱉기, '조금' 정렬
        pivot = a[high]  # 4
        left = low       # [0]
        for right in range(low, high):
            if a[right] < pivot:
                a[left], a[right] = a[right], a[left]
                left += 1
        a[left], a[high] = a[high], a[left]
        return left

    if low < high:  # 공집합일 땐 돌지 마라 (len == 2로 안 씀)
        pivot = partition(low, high)  # L을 뱉어내는 함수
        lomuto(low, pivot - 1)
        lomuto(pivot+1, high)


a = [2, 8, 7, 1, 3, 5, 6, 4]
lomuto(0, len(a)-1)
print(a)

# [2] 퀵정렬 - 호어(중간피봇)
# def hoare(low, high):
#     def partition(low, high):
#         pivot = (low + high) // 2
#         L = low
#         R = high
#
#         while L < R:
#             while a[L] < a[pivot] and L < R:
#                 L += 1
#             while a[R] >= a[pivot] and L < R:
#                 R -= 1
#             if L < R:
#                 if L == pivot:
#                     pivot = R
#                 a[L], a[R] = a[R], a[L]
#         a[pivot], a[R] = a[R], a[pivot]
#         return R
#
#     if low < high:
#         pivot = partition(low, high)
#         hoare(low, pivot-1)
#         hoare(pivot+1, high)
#
# a = [69, 10, 30, 2, 16, 8, 31, 22]
# hoare(0, len(a)-1)
# print(a)