def add_time(start, duration, day=False):
    start_hour, start_min, start_per = get_hour_minute(start, has_per=True)
    dur_hour, dur_min, dur_per = get_hour_minute(duration)
    if start_min + dur_min >= 60:
        add_hour = 1
        end_min = start_min + dur_min - 60
    else:
        add_hour = 0
        end_min = start_min + dur_min
    days_added = int((start_hour + add_hour + dur_hour) / 24)
    end_hour = (start_hour + add_hour + dur_hour) % 24
    if day:
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        end_day = f", {days[(days.index(day.lower()) + days_added) % 7].capitalize()}"
    else:
        end_day = "" 
    if end_hour >= 12:
        end_per = "PM"
        end_hour -= 12
    else:
        end_per = "AM"
    end_hour = 12 if end_hour == 0 else end_hour
    if days_added == 0:
        days_added = ""
    elif days_added == 1:
        days_added = " (next day)"
    else:
        days_added = f" ({int(days_added)} days later)"

    new_time = f"{end_hour}:{end_min:0>2} {end_per}" + end_day + days_added
    return new_time

def get_hour_minute(time, has_per=False):
    hour = int(time.split(":")[0])
    if has_per:
        minute = int(time.split(":")[1].split()[0])
        ampm = time.split(":")[1].split()[1]
        hour = hour if ampm == "AM" else hour + 12
    else:
        minute = int(time.split(":")[1])
        ampm = False
    return hour, minute, ampm

if __name__ == "__main__":
    print(add_time("11:40 AM", "0:25"))
