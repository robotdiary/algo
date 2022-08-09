test_case = int(input())
for T in range(1, test_case+1):
    box_num = int(input())
    boxes = list(map(int, input().split()))
    result = 0
    for box in range(box_num):
        count = 0
        for i in range(box+1, box_num):
            if boxes[box] > boxes[i]:
                count += 1
        if count > result:
            result = count
    print(f"#{T} {result}")
