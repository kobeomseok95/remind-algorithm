
def solution(num):
    count = 0
    while count < 500:
        if checkOne(num):
            return count
        num = calculateProcess(num)
        count += 1
    return -1


def calculateProcess(num):
    if checkEven(num):
        return num // 2
    return (num * 3) + 1


def checkEven(num):
    return num % 2 == 0


def checkOne(num):
    return num == 1


if __name__ == "__main__":
    print(solution(6))
    print(solution(16))
    print(solution(626331))
