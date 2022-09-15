# T = int(input())
# T = int(input())
# for tc in range(1, T+1):
#     line = int(input())
#
# # 1로 된 삼각형을 만든다
#     triangle = [[1]*i for i in range(1, line+1)]
#
# # 삼각형[셋째줄][두번째1]부터 (좌상단+우상단) 값으로 바꿔준다
#     for i in range(2, line):
#         for j in range(1, len(triangle[i])-1):
#             triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
#     print(f'#{tc}')
#
# # 출력
#     for answer in range(line):
#         print(*triangle[answer])

# [2] 다른 풀이
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 한 줄씩 만들어서 출력하고 싶었음
    a_list = [1, 1]
    # tc랑 첫 줄은 기본으로 출력하고
    print(f'#{tc}')
    print(1)
    # 둘째줄부터 삼각형이 나와야 하는 만큼 반복하면서 출력할건데용
    for i in range(n-1):
        print(*a_list)                  # 일단 출력하고
        b_list = []                     # 임시 리스트를 만들어서
        for j in range(len(a_list)-1):  # 리스트 안의 애들을 더해서 아랫줄을 만들겁니다
            b_list.append(a_list[j]+a_list[j+1])
        b_list = [1] + b_list + [1]    # 더한 값들의 앞 뒤를 1로 감싸준 후
        a_list = b_list                # 출력할 리스트를 변경하고 출력하러 ㄱㄱ
