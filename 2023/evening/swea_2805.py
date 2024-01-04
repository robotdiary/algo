# 농작물 수확하기
for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    answer = 0
    # 절반으로 나눠서 위랑 아래는 크기가 똑같으니까
    for i in range(n//2):
        answer += sum(arr[i][n//2-i:n//2+1+i])
        answer += sum(arr[n-1-i][n//2-i:n//2+1+i])

    # 중간 줄은 통채로 더해주기
    answer += sum(arr[n//2])
    print(answer)