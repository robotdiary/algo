def solution(s):
    answer = s
    word = ('zero','one','two','three','four','five','six','seven','eight','nine')
    num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    for i in range(10):
        if word[i] in answer:
            answer = answer.replace(word[i], num[word[i]])
    return int(answer)