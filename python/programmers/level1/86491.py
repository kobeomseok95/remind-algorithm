def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]
    answer = 0
    max_y, max_x = 0, 0
    for y, x in sizes:
        max_y = max(max_y, y)
        max_x = max(max_x, x)
        answer = max_y * max_x
    return answer
