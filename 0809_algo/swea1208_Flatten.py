for T in range(1, 11):
    count = int(input())
    boxes = list(map(int, input().split()))
    while count:
        for i in range(len(boxes)-1,0,-1):
            for j in range(0, i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
        if boxes[-1] - boxes[0] > 1:
            boxes[-1] -= 1 # 변수에다 할당해야지
            boxes[0] += 1
            count -= 1
            continue
        else:
            print(f"#{T} {boxes[-1] - boxes[0]}")
            break
    if count == 0:
        for i in range(len(boxes)-1,0,-1):
            for j in range(0, i):
                if boxes[j] > boxes[j+1]:
                    boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
        print(f"#{T} {boxes[-1] - boxes[0]}")