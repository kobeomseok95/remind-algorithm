from itertools import permutations


def solution(user_id, banned_id):
    answers = []
    for candidate_users in permutations(user_id, len(banned_id)):
        if contains(candidate_users, banned_id):
            candidate_users = set(candidate_users)
            if candidate_users not in answers:
                answers.append(candidate_users)
    return len(answers)


def contains(candidate_users, banned_ids):
    for i in range(len(banned_ids)):
        if not is_mapped(candidate_users[i], banned_ids[i]):
            return False
    return True


def is_mapped(user, banned_user_pattern):
    if len(user) != len(banned_user_pattern):
        return False
    for idx, ch in enumerate(banned_user_pattern):
        if ch == '*':
            continue
        if ch != user[idx]:
            return False
    return True
