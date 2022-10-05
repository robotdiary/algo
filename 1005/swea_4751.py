# swea 4751. 다솔이의 다이아몬드 장식 D3
for tc in range(1, int(input()) + 1):
    text = input()
    print(f'.{".#.." * len(text)}')
    print(f'.{"#.#." * len(text)}')
    answer = '#'
    for i in text:
        answer += f'.{i}.#'
    print(answer)
    print(f'.{"#.#." * len(text)}')
    print(f'.{".#.." * len(text)}')