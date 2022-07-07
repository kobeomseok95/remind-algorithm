def solution(play_time, adv_time, logs):
    play_time = str_to_sec(play_time)
    adv_time = str_to_sec(adv_time)
    cumulative_all_time = cumulate_log_time(play_time, logs)
    return get_proper_insert_adv_time(cumulative_all_time, play_time, adv_time)


def str_to_sec(time):
    hh, mm, ss = time.split(":")
    return int(ss) + int(mm) * 60 + int(hh) * 3600


def cumulate_log_time(play_time, logs):
    logs = sorted(logs)
    all_time = [0 for _ in range(play_time + 1)]
    for log in logs:
        start, end = log.split("-")
        start = str_to_sec(start)
        end = str_to_sec(end)
        all_time[start] += 1
        all_time[end] -= 1

    for _ in range(2):
        for i in range(1, len(all_time)):
            all_time[i] = all_time[i] + all_time[i - 1]

    return all_time


def get_proper_insert_adv_time(all_time, play_time, adv_time):
    adv_start_time, most_view = 0, 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                adv_start_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                adv_start_time = i - adv_time + 1
    return sec_to_str(adv_start_time)


def sec_to_str(second):
    time = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    return str(time).rjust(2, '0') + ":" + str(minute).rjust(2, '0') + ":" + str(second).rjust(2, '0')
