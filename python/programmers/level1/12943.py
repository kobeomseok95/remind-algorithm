def solution(num):
    answer = 0
    while num != 1 and answer < 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        answer += 1

    return answer if answer < 500 else -1


if __name__ == "__main__":
    print(solution(6))
    print(solution(16))
    print(solution(626331))
