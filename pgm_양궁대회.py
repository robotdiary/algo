def get_score(bullet, lion, apeach, idx, info, score):
    if not bullet:
        if score < lion - apeach:
            score = lion - apeach
        return
    if bullet - info[idx] - 1 >= 0:
        get_score(bullet - info[idx] - 1, lion + (10 - idx), apeach, idx + 1, info)
    get_score(bullet, lion, apeach + (10 - idx), idx + 1, info)
    return


def solution(n, info):
    answer = []
    score = 0
    get_score(n, 0, 0, 0, info, 0)
    return answer
