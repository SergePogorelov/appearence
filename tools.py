def group(lst):
    return [(lst[i - 1], lst[i]) for i in range(1, len(lst), 2)]


def get_seconds(time_list):
    seconds = set()

    for time in time_list:
        start = time[0]
        finsh = time[1] + 1
        seconds.update({i for i in range(start, finsh)})

    return seconds


def get_appearence(input_list):
    seconds_leson = get_seconds(group(input_list.get("lesson")))
    seconds_tutor = get_seconds(group(input_list.get("tutor")))
    seconds_pupil = get_seconds(group(input_list.get("pupil")))

    return len(seconds_tutor & seconds_pupil & seconds_leson)
