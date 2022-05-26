def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    for skill in skill_trees:
        skill_list_idx = 0
        for s in skill:
            if s in skill_list:
                if s != skill_list[skill_list_idx]:
                    break
                else:
                    skill_list_idx += 1
        else:
            answer += 1
    return answer
