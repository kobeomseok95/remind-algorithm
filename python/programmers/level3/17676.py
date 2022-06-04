def solution(lines):
    answer = 0
    start_times, end_times = [], []
    get_start_end_times(start_times, end_times, lines)
    for i in range(len(lines)):
        count = 0
        for j in range(i, len(lines)):
            if start_times[j] - 1000 < end_times[i]:
                count += 1
        answer = max(answer, count)
    return answer


def get_start_end_times(start_times, end_times, lines):
    for line in lines:
        day, s, t = line.split(" ")
        t = t[: -1]
        end_time = get_time(s)
        end_times.append(end_time)
        start_time = end_time - int(float(t) * 1000) + 1
        start_times.append(start_time)


def get_time(s):
    hour = int(s[: 2]) * 3600
    minute = int(s[3: 5]) * 60
    second = int(s[6: 8])
    millisecond = int(s[9:])
    return (hour + minute + second) * 1000 + millisecond
