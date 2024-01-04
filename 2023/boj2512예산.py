n = int(input())
requests = [0] + list(map(int, input().split()))
money = int(input())
answer = 0

sm = sum(requests)
mx = max(requests)
if sm <= money:
    answer = mx
else:
    requests.sort()
    for i in range(1, n + 1):  # [0] 추가해놓고 n까지 도는 거 적발
        if (requests[i] - requests[i - 1]) * (n - i + 1) <= money:
            money -= (requests[i] - requests[i - 1]) * (n - i + 1)
            answer = requests[i]
            if not money:
                break
        else:
            answer += money // (n - i + 1)
            break  # 탈출 안 해서 다음거 도는 거 적발

print(answer)