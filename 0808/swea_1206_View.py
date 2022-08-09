# 파일에서 데이터 읽어오기
# input() : 표준입출력에서 문자열 한 줄 읽어오기
# 표준 입력을 콘솔에서 파일로 
# import sys
# sts.stdin = open('파일이름','r') # 파일 열기 모드 : r > 읽기, w > 쓰기
import sys
sys.stdin = open("input.txt", "r")
# for _ in range(1, 11): # 테스트 케이스 수
#     N = int(input()) # 가로 길이
#     buildings = list(map(int, input().split())) # 빌딩의 높이
#     count = 0 # 조망권이 확보된 세대의 수
#     side_b = 0 #뺄 빌딩 높이
#     for b in range(2, N-2): # 빌딩의 갯수 만큼 반복
#         for i in range(-2, 3):
#             if side_b < buildings[b+i]: #side_b를 앞에 써줌
#                 side_b = buildings[b+i]
#         if buildings[b] - side_b > 0:
#             count += (buildings[b] - side_b)
#     print(f'#{_} {count}')

# for tc in range(1,11):
#     N = int(input())    #테스트케이스 입력 길이
#     buildings = list(map(int, input().split())) # 빌딩정보
#     result = 0 # 조망권이 확보된 세대 수
#     for i in range(2, N-2):
#         # 양쪽 2칸안에 있는 이웃 빌딩들 중 제일 큰 빌딩 찾기
#         neighbor = [buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]]
#         max_height = 0  #최대값 찾을 때, 최대값을 저장하는 변수는 가능한 작은수로 초기화
#         for b in neighbor:
#             if max_height < b:
#                 max_height = b
#         # max_height 보다 현재 건물(buildings[i])의 높이가 높으면 조망권이 확보된 세대가 있음
#         if buildings[i] > max_height:
#             result += (buildings[i] - max_height)
#     print(f'#{tc} {result}')

# for T in range(1, 11):
#     N = int(input())
#     buildings = list(map(int, input().split())) # 빌딩의 높이
#     count = 0 # 조망권이 확보된 세대의 수
#     for b in range(2, N-2): # 빌딩의 갯수 만큼 반복
#         side_b = 0 #뺄 빌딩 높이  
#         for i in range(-2, 3):
#             if buildings[b+i] != buildings[b] and buildings[b+i] > side_b: #본인일 때 제외, 가장 높은 빌딩을 선택
#                 side_b = buildings[b+i]
#         if buildings[b] - side_b > 0:
#             count += (buildings[b] - side_b)
#     print(f'#{T} {count}')

for T in range(1, 11):
    N = int(input())    #테스트케이스 길이
    buildings = list(map(int, input().split())) # 빌딩의 높이
    count = 0 # 조망권이 확보된 세대의 수
    for b in range(2, N-2):
        # 양쪽 2칸안에 있는 이웃 빌딩들 중 제일 큰 빌딩 찾기
        side_list = [buildings[b-2], buildings[b-1], buildings[b+1], buildings[b+2]]
        side_b = 0  # 뺄 빌딩의 높이
        for i in side_list:
            if i > side_b:
                side_b = i
        if buildings[b] - side_b > 0:
            count += (buildings[b] - side_b)
    print(f'#{T} {count}')