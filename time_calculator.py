def add_time(start, duration, day='none'):
    allowed = '0123456789'
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_time = ''
    hours = ''
    minutes = ''
    days = 0
    proceed = False
    hours_2 = ''
    minutes_2 = ''
    proceed_2 = False
    is_morning = True

    for char in start:  # parse for minutes, hour, and AM/PM in the start time
        if char != ':' and char != ' ' and not proceed:
            hours = hours + char
            continue
        elif char == ':' and not proceed:
            proceed = True
            continue
        elif (char in allowed) and proceed:
            minutes = minutes + char
            continue
        elif char not in allowed and proceed and char != ' ':
            if char == 'A':
                is_morning = True
            else:
                is_morning = False
            break

    for char in duration:  # parse for minutes, hour, and AM/PM in the duration time
        if char != ':' and char != ' ' and not proceed_2:
            hours_2 = hours_2 + char
            continue
        elif char == ':' and not proceed_2:
            proceed_2 = True
            continue
        elif (char in allowed) and proceed_2:
            minutes_2 = minutes_2 + char
            continue

    while int(hours_2) > 0:
        if int(hours_2) >= 12:
            hours_2 = str(int(hours_2) - 12)
            if is_morning:
                is_morning = False
            else:
                is_morning = True
                days = days + 1
            continue
        elif int(hours_2) >= 12 - int(hours) and int(hours) < 12:
            hours_2 = str(int(hours_2) - (12 - int(hours)))
            hours = '12'
            if is_morning:
                is_morning = False
            else:
                is_morning = True
                days = days + 1
            continue
        elif int(hours_2) > 0 and int(hours) == 12:
            hours = '1'
            hours_2 = str(int(hours_2) - 1)
        else:
            hours = str(int(hours) + int(hours_2))
            hours_2 = '0'

    if int(minutes_2) > 59 - int(minutes):  # if need be, roll the hour over
        minutes_2 = str(int(minutes_2) - (60 - int(minutes)))
        minutes = '00'
        if int(hours) == 11:  # the two special cases are when it is 11 or 12
            hours = '12'
            if is_morning:
                is_morning = False
            else:
                is_morning = True
                days = days + 1
        else:
            if int(hours) == 12:
                hours = '1'
            else:
                hours = str(int(hours) + 1)

    minutes = str(int(minutes) + int(minutes_2))
    if int(minutes) < 10:
        minutes = '0' + minutes

    new_time = new_time + hours + ':' + minutes
    if is_morning:
        new_time = new_time + ' AM'
    else:
        new_time = new_time + ' PM'
    if day != 'none':
        for x in week:
            if day.lower().capitalize() == x:
                day_of_the_week = week.index(x)
                break
        final = (day_of_the_week + days) % 7
        new_time = new_time + ', ' + week[final]
    if days == 1:
        new_time = new_time + ' (next day)'
    if days > 1:
        new_time = new_time + ' (' + str(days) + ' days later)'

    return new_time
