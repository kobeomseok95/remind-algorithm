def solution(a, b):
    day_dict = {
        0: "THU",
        1: "FRI",
        2: "SAT",
        3: "SUN",
        4: "MON",
        5: "TUE",
        6: "WED"
    }
    months = [
        0, 31, 29, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31
    ]
    days = 0
    for month in range(1, a):
        days += months[month]
    days += b
    return day_dict[days % 7]


if __name__ == "__main__":
    print(solution(5, 24))
