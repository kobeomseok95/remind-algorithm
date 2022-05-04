def solution(s):
    if len(s) % 2 != 0:
        return 0

    bracket_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    answer = 0
    for i in range(len(s)):
        if is_correct(s, bracket_dict):
            answer += 1
        s = rotate(s)
    return answer


def is_correct(string, bracket_dict):
    stack = []
    for s in string:
        if not stack and s not in bracket_dict:
            return False

        if s in bracket_dict:
            stack.append(s)
        else:
            if bracket_dict[stack[-1]] == s:
                stack.pop()
            else:
                return False
    return not stack


def rotate(string):
    return string[1:] + string[0]
