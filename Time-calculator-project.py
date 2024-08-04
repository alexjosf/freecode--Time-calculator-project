def add_time(start, duration, day = None):

    start_h = int(start.split(" ")[0].split(":")[0])
    start_m = int(start.split(" ")[0].split(":")[1])
    start_format = start.split(" ")[1]
    duration_h = int(duration.split(':')[0])
    duration_m = int(duration.split(':')[1]) 

    days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    if (start_format == 'PM'):
        start_h += 12

    total_m = (start_m + duration_m)%60
    total_h = start_h + duration_h + ((start_m + duration_m) // 60)

    final_h = (total_h % 24)%12

    if final_h == 0:
        final_h = 12
    final_h = str(final_h)

    total_d = (total_h // 24)

    if (total_h % 24) <= 11:
        mid_d = "AM"
    else:
        mid_d = "PM"

    if total_m < 10:
        final_m = "0" + str(total_m)
    else:
        final_m = str(total_m)

    final_timestamp = final_h + ":" + final_m + " " + mid_d

    if (day == None):
        if (total_d == 0):
            return final_timestamp
        if (total_d == 1):
            return final_timestamp + " (next day)"
        return final_timestamp + " (" + str(total_d) + " days later)"
    else:
        final_wd = (days[day.lower().capitalize()] + total_d) % 7
        for i, j in days.items():
            if j == final_wd:
                final_wd = i
                break
        if (total_d == 0):
            return final_timestamp + ", " + final_wd
        if (total_d == 1):
            return final_timestamp + ", " + final_wd + " (next day)"
        return final_timestamp + ", " + final_wd + " (" + str(total_d) + " days later)"


print(add_time('3:00 PM', '3:10'))