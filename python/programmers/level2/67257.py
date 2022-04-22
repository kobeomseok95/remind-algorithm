from itertools import permutations
import re


def solution(expression):
    answer = []
    operator_combinations = create_operator_combinations(expression)
    for combination in operator_combinations:
        operands = re.split('[*+-]', expression)
        operators = re.split('[0-9]+', expression)[1: -1]
        for pick_operator in combination:
            while pick_operator in operators:
                idx = operators.index(pick_operator)
                operands[idx] = str(eval(operands[idx] + pick_operator + operands[idx + 1]))
                operators.pop(idx)
                operands.pop(idx + 1)
        answer.append(abs(int(operands[0])))
    return max(answer)


def create_operator_combinations(expression):
    operator_set = set()
    for e in expression:
        if not e.isdigit():
            operator_set.add(e)
    return list(permutations(operator_set, len(operator_set)))
