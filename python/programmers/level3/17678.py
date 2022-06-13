def solution(n, t, m, timetable):
    crew_time = sorted([int(time[: 2]) * 60 + int(time[3:]) for time in timetable])
    bus_time = [9 * 60 + t * i for i in range(n)]
    answer = 0
    crew_idx = 0
    for time in bus_time:
        count = 0
        while count < m and crew_idx < len(crew_time) and crew_time[crew_idx] <= time:
            crew_idx += 1
            count += 1
        if count < m:
            answer = time
        else:
            answer = crew_time[crew_idx - 1] - 1
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
