def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split(" ")[1]] += 1

    for r in set(report):
        report_user, reported_user = r.split(" ")
        if reports[reported_user] >= k:
            answer[id_list.index(report_user)] += 1

    return answer



























if __name__ == "__main__":
    print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2
    ))
    print(solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3
    ))
