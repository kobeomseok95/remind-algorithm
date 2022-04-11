def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.add(numbers[i] + numbers[j])

    return sorted(list(answer))




























if __name__ == "__main__":
    print(solution([2, 1, 3, 4, 1]))
    print(solution([5, 0, 2, 7]))
