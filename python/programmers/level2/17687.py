def solution(n, t, m, p):
    answer, test = '', ''
    number_list = "0123456789ABCDEF"
    for i in range(m * t):
        test += str(convert(i, n, number_list))
    while len(answer) < t:
        answer += test[p - 1]
        p += m
    return answer


def convert(number, radix, number_list):
    div, mod = divmod(number, radix)
    if div == 0:
        return number_list[mod]
    else:
        return convert(div, radix, number_list) + number_list[mod]
