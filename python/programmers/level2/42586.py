"""
def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while progresses:
        for i in range(len(progresses) - 1, -1, -1):
            progresses[i] += speeds[i]
        pop_count = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            pop_count += 1
        answer.append(pop_count) if pop_count > 0 else pop_count
    return answer
"""
def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        take_job_complete_day = -((p - 100) // s)
        if not answer or answer[-1][0] < take_job_complete_day:
            answer.append([take_job_complete_day, 1])
        else:
            answer[-1][1] += 1
    return [a[1] for a in answer]
