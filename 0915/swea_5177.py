# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 (D2)
def heap_push(item):
    heap.append(item)
    child_idx = len(heap) - 1
    parent_idx = child_idx // 2
    while parent_idx and heap[parent_idx] > heap[child_idx]:
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
        child_idx = parent_idx
        parent_idx = child_idx // 2


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = ['최소힙 :']
# [1] 인풋 리스트를 모두 힙리스트에 추가
    for i in nums:
        heap_push(i)
# [2] 마지막 인덱스를 찾아서
    end_idx = len(heap) - 1
# [3] 부모(인덱스//2)를 구해서 더하기 루트까지 반복
    answer = 0
    while end_idx > 1:
        answer += int(heap[end_idx // 2])
        end_idx = end_idx // 2
    print(f'#{tc} {answer}')

# 최소힙 구현
# [1] 삽입
# def heap_push(item):
#     heap.append(item)
#     child_idx = len(heap) - 1
#     parent_idx = child_idx // 2
#     # 루트 노드 (1번 인덱스) 까지 and
#     while parent_idx and heap[parent_idx] > heap[child_idx]:
#         heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
#         child_idx = parent_idx
#         parent_idx = child_idx // 2


# [2] 삭제
# def heap_pop():
#     # pop할 게 하나도 없으면 못 하도록
#     if len(heap) == 1:
#         return
#     # pop은 리턴값이 있어야 하니까 디폴트 첫째값
#     result = heap[1]
#     # 맨 뒤를 빈 칸으로 가져다 놓고
#     heap[1] = heap.pop()
#     # 아래로 가면서 정렬
#     parent = 1
#     # 일단 왼쪽 자식을 기준으로 하고
#     child = parent * 2
#     # 오른쪽 노드랑 비교해서 더 작은 값으로 지정
#     # 오른쪽 노드가 범위 안인지 확인하고
#     if child + 1 <= len(heap)-1:
#         # 더 작은 애면 더 작은 애랑 바꿀 준비
#         if heap[child] > heap[child + 1]:
#             child += 1
#     # 끝 노드 (인덱스) 까지 and
#     while child <= len(heap)-1 and heap[parent] > heap[child]:
#         heap[parent], heap[child] = heap[child], heap[parent]
#         parent = child
#         child = parent * 2
#         if child + 1 <= len(heap) - 1:
#             if heap[child] > heap[child + 1]:
#                 child += 1
#     return result

# 힙은 완전이진트리

# 왼쪽부터 차례로 쌓이기 때문에
# (트리를 리스트로 표현할 때)
# 리스트에 append 가능
# 삽입 : 맨 뒤에 삽입 (append) 부모를 보고 스왑 스왑 (x, y = y, x)
# 제거 : 제거(pop(0))한 자리에 맨 뒤 요소 가져와서 아래로 더 작은 애랑 스왑 스왑

# [2] 최대힙 구현
