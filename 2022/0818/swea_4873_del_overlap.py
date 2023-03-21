T = int(input())
for tc in range(1, T+1):
    check = input() # ABCCB
    idx = 0
# 문자열[0]부터 [뒤에서 두번째]까지 반복하겠다.
    while idx < len(check)-1:
    # for i in range(len(check)-1): 하면 중간에 문자열이 사라져서 Indexerror
    # while idx < len(check): 하면 문자열 마지막 인덱스까지 가서 Indexerror

# 뒤에 거랑 같으면 삭제
        if check[idx] == check[idx+1]:
            check = check.replace(check[idx:idx+2], '') # 얘는 문자열 밖의 인덱스까지 가도 에러 안 남
# 삭제하고 다시 앞에서부터 확인해야 하니까 idx = 0으로 초기화
            idx = 0
# 뒤에 거랑 다르면 그 다음 애를 확인해야하니까 idx + 1
        else:
            idx += 1

    print(f'#{tc} {len(check)}')
