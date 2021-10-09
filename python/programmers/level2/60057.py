def solution(string):
    answer = len(string)
    maxDivide = len(string) // 2
    for interval in range(1, maxDivide + 1):
        answer = min(answer, compress(string, interval))
    return answer


def compress(string, interval):
    count = 1
    compressed = ''
    for i in range(0, len(string), interval):
        front = string[i: i+interval]
        back = string[i+interval: i+(2*interval)]

        if front == back:
            count += 1
        else:
            compressed += (str(count) if count != 1 else '') + front
            count = 1
    return len(compressed)


if __name__ == "__main__":
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
    print(solution("abcabcdede"))
    print(solution("abcabcabcabcdededededede"))
    print(solution("xababcdcdababcdcd"))
