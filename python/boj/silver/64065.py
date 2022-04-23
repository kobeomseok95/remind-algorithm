def solution(s):
    a = sorted([s.split(",") for s in s[2: -2].split("},{")], key=len)
    answer = []
    for sets in a:
        for x in sets:
            if int(x) not in answer:
                answer.append(int(x))
                break
    return answer
