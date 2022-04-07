def solution(numbers, hand):
    hand_coordinate = create_hand_coordinate_dict()
    left, right = hand_coordinate['*'], hand_coordinate['#']
    answer = ''
    for number in numbers:
        location = hand_coordinate[str(number)]
        result_hand = handling(left, right, hand, location)
        if result_hand == "L":
            left = location
        else:
            right = location
        answer += result_hand

    return answer


def create_hand_coordinate_dict():
    dial_array = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    hand_coordinate = dict()
    for i in range(len(dial_array)):
        for j in range(len(dial_array[0])):
            hand_coordinate[dial_array[i][j]] = (i, j)
    return hand_coordinate


def handling(left, right, hand, location):
    if location[1] == 0:
        return "L"
    elif location[1] == 2:
        return "R"
    else:
        left_dist = abs(location[0] - left[0]) + abs(location[1] - left[1])
        right_dist = abs(location[0] - right[0]) + abs(location[1] - right[1])
        if left_dist > right_dist:
            return "R"
        elif left_dist < right_dist:
            return "L"
        else:
            if hand == "left":
                return "L"
            else:
                return "R"





if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
