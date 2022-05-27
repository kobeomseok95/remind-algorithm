def solution(m, musicinfos):
    music_dict = dict()
    m = replace_sheet_code(m)
    for idx, music_info in enumerate(musicinfos):
        start, end, name, sheet = music_info.split(",")
        sheet = replace_sheet_code(sheet)
        play_time = get_play_time(start, end)
        play_sheet = get_sheet_by_playtime(play_time, sheet)
        music_dict[name] = (play_time, idx, play_sheet)
    answers = []
    for name, play_info in music_dict.items():
        play_time, play_order, play_sheet = play_info
        if m in play_sheet:
            answers.append((name, play_time, play_order))
    return sorted(answers, key=lambda x: (-x[1], x[2]))[0][0] if answers else "(None)"


def replace_sheet_code(codes):
    return codes.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('A#', 'a').replace('E#', 'e')


def get_play_time(start, end):
    start_hour, start_minute = start.split(":")
    end_hour, end_minute = end.split(":")
    return abs(int(start_hour) - int(end_hour)) * 60 + (int(end_minute) - int(start_minute))


def get_sheet_by_playtime(play_time, sheet):
    play_sheet = ""
    idx = 0
    for i in range(play_time):
        play_sheet += sheet[idx]
        idx = (idx + 1) % len(sheet)
        if sheet[idx] == '#':
            play_sheet += sheet[idx]
            idx = (idx + 1) % len(sheet)
    return play_sheet
