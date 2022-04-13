def solution(s, n):
    lower_idx = 97
    upper_idx = 65
    answer = []
    for c in s:
        if c.islower():
            answer.append(chr(((ord(c) - lower_idx + n) % 26) + lower_idx))
        elif c.isupper():
            answer.append(chr(((ord(c) - upper_idx + n) % 26) + upper_idx))
        else:
            answer.append(c)
    return ''.join(answer)
