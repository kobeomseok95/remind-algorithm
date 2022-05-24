def solution(s):
    convert_count, zero_count = 0, 0
    while s != "1":
        convert_count += 1
        zero_count += s.count("0")
        s = s.replace("0", "")
        s = str(bin(len(s)))[2:]
    return [convert_count, zero_count]
