def make_readable(seconds):
    hours = seconds//3600
    if hours < 10:
        hours = str(0)+str(hours)
    rem1 = seconds % 3600
    mins = rem1 // 60
    if mins < 10:
        mins = str(0)+str(mins)
    seconds = rem1 % 60
    if seconds <10:
        seconds = str(0)+str(seconds)
    time = str(hours) + ":" + str(mins) + ":" + str(seconds)
    return time