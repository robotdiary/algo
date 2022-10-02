#  1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 D3
import sys; sys.stdin = open('input.txt', 'r')
# input().rstrip('0') 인풋에서 둘러쌓인 0을 빈 칸으로 만들어줌(위, 아래, 뒤)
pattern = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    quest = []
    start = 0
    code = []
    # [1] 암호문 한 줄 건져오기
    for i in range(n):
        if '1' in arr[i]:
            quest = arr[i]
            break
    # [2] 시작 위치 찾기
    for i in range(len(quest)-1, -1, -1):
        if quest[i] == '1':
            start = i - 55
            break
    # [3] start부터 7자리씩 잘라서 읽기
    for i in range(start, start + 50, 7):
        code.append(pattern[quest[i: i + 7]])
    # # [4] 홀수 * 3 + 짝수가 10의 배수인 경우 확인
    if (sum(code[0:8:2]) * 3 + sum(code[1:8:2])) % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(code)}')
    # print((sum(code[0:8:2]) * 3 + sum(code[1:8:2])))

# code = [8,8,0,1,2,3,4,6]
#     print(code[0:7:2], sum(code[0:7:2])*3)
#     print(code[1:9:2], sum(code[1:9:2]))