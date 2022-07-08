def solution(n, build_frame):
    frames = set()
    for x, y, a, build in build_frame:
        frame = (x, y, a)
        if build:
            frames.add(frame)
            if impossible(frames):
                frames.remove(frame)
        elif frame in frames:
            frames.remove(frame)
            if impossible(frames):
                frames.add(frame)

    frames = map(list, frames)
    return sorted(frames, key=lambda x: (x[0], x[1], x[2]))


def impossible(frames):
    COLUMN, BEAM = 0, 1
    for x, y, a in frames:
        if a == COLUMN:
            if y != 0 and (x, y - 1, COLUMN) not in frames and (x - 1, y, BEAM) not in frames and (x, y, BEAM) not in frames:
                return True
        else:
            if ((x - 1, y, BEAM) not in frames or (x + 1, y, BEAM) not in frames) and \
                    (x, y - 1, COLUMN) not in frames and (x + 1, y - 1, COLUMN) not in frames:
                return True
    return False
