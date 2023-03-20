# 10804. 문자열의 거울상 D3
mirror = {
    'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
}
T = int(input())
for tc in range(1, 1 + T):
    quest = input()
    answer = ''
# 문자열을 거꾸로 돌면서 딕셔너리 해당 값을 answer에 추가
    for i in range(len(quest)):
        answer += mirror[quest[-1-i]]
    print(f'#{tc} {answer}')