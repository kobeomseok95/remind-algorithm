def solution(brown, yellow):
    h = 1
    w = (brown // 2) - 1
    while w >= h:
        if w * (h + 2) == brown + yellow:
            return [w, h + 2]
        w -= 1
        h += 1
