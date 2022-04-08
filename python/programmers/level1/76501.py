def solution(absolutes, signs):
    return sum(absolutes if signs else -absolutes for absolutes, signs in zip(absolutes, signs))
