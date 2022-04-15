def solution(string):
    answer = len(string)
    for interval in range(1, len(string) // 2 + 1):
        interval_string = ''
        repeat_count = 1
        compressed_length = 0
        for i in range(0, len(string), interval):
            temp = string[i: i+interval]
            if temp == interval_string:
                repeat_count += 1
            else:
                compressed_length += len(temp)
                if repeat_count > 1:
                    compressed_length += len(str(repeat_count))
                repeat_count = 1
                interval_string = temp
        if repeat_count > 1:
            compressed_length += len(str(repeat_count))
        answer = min(answer, compressed_length)
    return answer
