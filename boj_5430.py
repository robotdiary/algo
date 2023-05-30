import sys

for tc in range(int(sys.stdin.readline().rstrip())):
    p = sys.stdin.readline().rstrip()  # 수행할 함수
    n = int(sys.stdin.readline().rstrip())  # 수의 개수
    num_list = []
    if n:
        num_list = list(map(int, sys.stdin.readline().rstrip().strip("[]").split(",")))
    else:
        throw = sys.stdin.readline()
    # 버리는 수가 배열보다 더 많으면 error
    if p.count("D") > n:
        print("error")
    else:
        reverse = 0  # 뒤집을 건지
        r_count = 0  # 연속한 r의 수
        start = 0
        end = 0
        if n:
            end = len(num_list)-1
        for func in range(len(p)):
            if p[func] == "R":
                r_count += 1
            else:
                # 뒤집어서 버리기면
                if r_count % 2:
                    reverse += 1
                    if reverse % 2:
                        end -= 1
                    else:
                        start += 1
                # 안 뒤집고 버리기면
                else:
                    if reverse % 2:
                        end -= 1
                    else:
                        start += 1
                r_count = 0
        if p.count("R") % 2:
            if start:
                print(str(num_list[end:start-1:-1]).replace(" ", ""))
            else:
                print(str(num_list[end::-1]).replace(" ", ""))
        else:
            if end < len(num_list) - 1:
                print(str(num_list[start:end + 1]).replace(" ", ""))
            else:
                print(str(num_list[start::]).replace(" ", ""))