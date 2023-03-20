# 큐 연습문제 - 큐의 구현
# def enQueue(item):
#     global rear
#     if isFull():
#         print('Queue_Full')
#     else:
#         rear += 1
#         Q[rear] = item
#
# class try_Queue:
def enqueue(item):
    global try_queue
    try_queue.append(item)

def dequeue():
    global try_queue
    if try_queue:
        print(try_queue.pop(0))
    else:
        print("queue is empty")

try_queue = []

enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
dequeue()
dequeue()