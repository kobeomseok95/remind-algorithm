def solution(x):
    return x % sum(list(map(int, str(x)))) == 0


if __name__ == "__main__":
    print(solution(10))
    print(solution(11))
    print(solution(12))
    print(solution(13))
