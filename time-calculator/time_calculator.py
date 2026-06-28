"""
Time Calculator

Adds a duration to a given start time while correctly handling
AM/PM conversion, day rollover, and optional weekdays.
"""


def add_time(start, duration, day=None):
    time, period = start.split()
    start_hour, start_min = map(int, time.split(":"))

    # Convert start time to 24-hour format
    if period == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12

    dur_hour, dur_min = map(int, duration.split(":"))

    start_total = start_hour * 60 + start_min
    duration_total = dur_hour * 60 + dur_min

    total_minutes = start_total + duration_total

    days_passed = total_minutes // 1440
    remaining_minutes = total_minutes % 1440

    new_hour_24 = remaining_minutes // 60
    new_min = remaining_minutes % 60

    # Convert back to 12-hour format
    if new_hour_24 == 0:
        new_hour = 12
        new_period = "AM"
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = "AM"
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = "PM"
    else:
        new_hour = new_hour_24 - 12
        new_period = "PM"

    new_time = f"{new_hour}:{new_min:02d} {new_period}"

    if day:
        days_list = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        current_index = days_list.index(day.capitalize())
        new_index = (current_index + days_passed) % 7
        new_time += f", {days_list[new_index]}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

if __name__ == "__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))