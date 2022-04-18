def solution(s):
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()

    return int(not stack)
