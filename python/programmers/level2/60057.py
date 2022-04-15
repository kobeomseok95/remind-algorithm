def solution(string):
    answer = len(string)
    for interval in range(1, len(string) // 2 + 1):
        compressed_string = ''
        compressed_length = 0
        repeat_count = 1
        for i in range(0, len(string), interval):
            temp = string[i: i+interval]
            if compressed_string == temp:
                repeat_count += 1
            else:
                compressed_length += len(temp)
                if repeat_count > 1:
                    compressed_length += len("{}".format(repeat_count))
                repeat_count = 1
                compressed_string = temp
        if repeat_count > 1:
            compressed_length += len("{}".format(repeat_count))
        answer = min(answer, compressed_length)
    return answer


























if __name__ == "__main__":
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
    print(solution("abcabcdede"))
    print(solution("abcabcabcabcdededededede"))
    print(solution("xababcdcdababcdcd"))
