def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    return [-1] if not answer else sorted(answer)
