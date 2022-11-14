# 나는야 포켓몬 마스터 이다솜
import sys
n, m = map(int, sys.stdin.readline().split())  # 도감에 수록된 수, 문제 수
pokemons = [sys.stdin.readline() for _ in range(n)]
for tc in range(1, m + 1):
    target = sys.stdin.readline()
    if target.isdigit():
        print(pokemons[int(target) - 1])
    else:
        print(pokemons.index(target) + 1)