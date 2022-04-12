def solution(dartResult):
    areas = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    scores = []
    before_idx = -1
    dartResult = dartResult.replace("10", "X")
    slices = ["10" if d == "X" else d for d in dartResult]
    for s in slices:
        if s in areas:
            scores[-1] **= areas[s]
        elif s == "*":
            scores[-1] *= 2
            if before_idx != 0:
                scores[-2] *= 2
        elif s == "#":
            scores[-1] *= -1
        else:
            scores.append(int(s))
            before_idx = len(scores) - 1

    return sum(scores)
