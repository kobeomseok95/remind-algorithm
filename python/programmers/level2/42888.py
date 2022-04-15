def solution(record):
    user_id_nickname_dict = dict()
    answer = []
    for r in record:
        split_record = r.split()
        if split_record[0] == "Enter":
            user_id_nickname_dict[split_record[1]] = split_record[2]
        elif split_record[0] == "Change":
            user_id_nickname_dict[split_record[1]] = split_record[2]
    for r in record:
        split_record = r.split()
        if split_record[0] == "Enter":
            answer.append(f"{user_id_nickname_dict[split_record[1]]}님이 들어왔습니다.")
        elif split_record[0] == "Leave":
            answer.append(f"{user_id_nickname_dict[split_record[1]]}님이 나갔습니다.")
    return answer
