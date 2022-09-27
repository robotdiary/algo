# 5204 - 병합 정렬
def merge_sort(input_list):  # 쪼개기
    if len(input_list) == 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]   # 인덱스 번호 잘 봐봐
    right_half = input_list[mid:]  # 슬라이싱으로 새로운 id 생성

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def merge(left, right):  # 붙이기
    global answer

    result = [0] * (len(left) + len(right))  # 틀, 새로운 id
    l = r = idx = 0

    if left[-1] > right[-1]:
        answer += 1
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1
    # 한 쪽의 인덱스가 끝나서 터졌을 때, 남은 애 넣기
    # pop으로 뺐으면 남은 건 extend로 넣을 수 있음
    while l < len(left):
        result[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        result[idx] = right[r]
        r += 1
        idx += 1

    return result


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[n//2]} {answer}')
