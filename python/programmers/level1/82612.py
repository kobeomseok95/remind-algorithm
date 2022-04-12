def solution(price, money, count):
    for i in range(1, count + 1):
        multiple_price = price * i
        money -= multiple_price
    return abs(money) if money < 0 else 0


if __name__ == "__main__":
    print(solution(3, 20, 1))
