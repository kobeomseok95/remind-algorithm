def solution(number, k):
    number = list(number)
    answer = [number.pop(0)]
    for n in number:
        if answer[-1] < n:
            while answer and answer[-1] < n and k > 0:
                answer.pop()
                k -= 1
            answer.append(n)
        elif k == 0 or answer[-1] >= n:
            answer.append(n)
    if k:
        answer = answer[:-k]
    return ''.join(answer)
