test_case = int(input())
for T in range(1, test_case+1):
    box_num = int(input())
    boxes = list(map(int, input().split()))
    result = 0
    # 전체 박스만큼 반복
    for box in range(box_num):
        count = 0
    # 선택된 박스 오른쪽과만 비교
        for i in range(box+1, box_num):
            if boxes[box] > boxes[i]:
                count += 1
    #가장 큰 값만 저장하고 나머지는 버림
        if count > result:
            result = count
    print(f"#{T} {result}")