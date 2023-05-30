from collections import defaultdict


def solution(survey, choices):
    answer = ''
    result_dict = defaultdict()
    for char_type in list("RTCFJMAN"):
        result_dict[char_type] = 0

    for i in range(len(survey)):
        left, right = survey[i]
        if choices[i] == 1:
            result_dict[left] += 3
        elif choices[i] == 2:
            result_dict[left] += 2
        elif choices[i] == 3:
            result_dict[left] += 1
        else:
            result_dict[right] += choices[i] % 4

    for j in ["RT", "CF", "JM", "AN"]:
        left, right = j
        if result_dict[left] == result_dict[right]:
            answer += chr(min(ord(left), ord(right)))
        elif result_dict[left] > result_dict[right]:
            answer += left
        else:
            answer += right

    return answer