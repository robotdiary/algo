# 연습 문제1 선택 정렬 함수를 재귀적 알고리즘으로 작성
def SelectionSort(A, s):
    if s == len(A)-1:
        return
    min_x = s
    for i in range(s + 1, len(A)):
        if A[min_x] > A[i]:
            min_x = i
    A[s], A[min_x] = A[min_x], A[s]
    SelectionSort(A, s + 1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
SelectionSort(A, 0)
print(A)