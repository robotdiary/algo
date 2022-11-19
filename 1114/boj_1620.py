# # 나는야 포켓몬 마스터 이다솜
# import sys
# input = sys.stdin.readline
n, m = map(int, input().split())  # 도감에 수록된 수, 문제 수
pokemons = dict()
pokemons_num = dict()
for i in range(1, n + 1):
    pokemon = input().strip()
    pokemons[i] = pokemon
    pokemons_num[pokemon] = i
for _ in range(m):
    target = input().strip()
    if target.isdigit():
        print(pokemons[int(target)])
    else:
        print(pokemons_num[target])
