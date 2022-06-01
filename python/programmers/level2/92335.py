from math import sqrt


def solution(n, k):
    converted_number = convert(n, k)
    answer = 0
    for num in converted_number.split('0'):
        check_number = 0 if num == '' else int(num)
        if check_number >= 2 and is_prime(check_number):
            answer += 1
    return answer


def convert(n, k):
    div, mod = divmod(n, k)
    if div == 0:
        return str(mod)
    else:
        return convert(div, k) + str(mod)


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(solution(437674, 3))
    print(solution(110011, 10))
    print(solution(36, 3))
