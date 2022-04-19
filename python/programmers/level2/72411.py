from itertools import combinations


def solution(orders, course):
    answer = []
    for size in course:
        order_combinations = []
        for order in orders:
            order_combinations.extend(combinations(list(sorted(order)), size))

        order_comb_count_dict = dict()
        for order_combination in order_combinations:
            order_str = ''.join(order_combination)
            if order_str not in order_comb_count_dict:
                order_comb_count_dict[order_str] = 0
            order_comb_count_dict[order_str] += 1

        max_count = max(order_comb_count_dict.values()) if order_comb_count_dict else 0
        if max_count > 1:
            for order_str, count in order_comb_count_dict.items():
                if count == max_count:
                    answer.append(order_str)
    return sorted(answer)
