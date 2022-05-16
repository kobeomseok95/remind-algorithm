def solution(numbers):
    answer = []
    for x in numbers:
        answer.append(f(x))
    return answer


def f(number):
    if number % 2 == 0:
        return number + 1
    else:
        bin_number = '0' + bin(number)[2:]
        zero_idx = bin_number.rfind('0')
        bin_number = list(bin_number)
        bin_number[zero_idx] = '1'
        bin_number[zero_idx + 1] = '0'
        return int('0b' + ''.join(bin_number), 2)
