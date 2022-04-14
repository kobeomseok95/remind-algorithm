def solution(inputs):
    a, b = inputs.split(" ")
    a = int(a)
    b = int(b)
    answer = ""
    for i in range(b):
        for j in range(a):
            answer += "*"
        answer += "\n"
    return answer
