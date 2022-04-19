import sys
sys.setrecursionlimit(10**6)


def solution(p):
    if p == '':
        return ''

    left, right = 0, 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        u += p[i]
        if left == right:
            v = p[i+1:]
            break

    if correct(u):
        return u + solution(v)
    else:
        rev = ''
        for c in u[1: -1]:
            if c == '(':
                rev += ')'
            else:
                rev += '('
        return '(' + solution(v) + ')' + rev


def correct(u):
    stack = []
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            return False if not stack else stack.pop()
    return not stack
