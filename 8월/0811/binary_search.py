def binarySearch(book, key):
    count = 0
    pages = list(range(1, book+1))
    start = 1
    end = book
    while start <= end:
        middle = (start + end)//2
        if pages[middle-1] == key: # 인덱스와 페이지를 잘 생각해보자
            return count
        elif pages[middle-1] > key:
            end = middle
        else:
            start = middle
        count += 1 # 어떤 경우도 페이지는 찾아지니까 카운트 수를 리턴

T = int(input())
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())
    if binarySearch(p, pa) < binarySearch(p, pb):
        print(f'#{tc} A')
    elif binarySearch(p, pa) > binarySearch(p, pb):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')