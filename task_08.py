def minutes_to_hours(minutes):
    calc_hours = minutes // 60
    calc_minutes = minutes % 60
    hours = str(calc_hours)
    mins =  str(calc_minutes)
    if calc_hours == 1:
        print( hours +" hour", ",", " ", end="")
    elif calc_hours >= 0:
        print(hours +" hours", ",", " ", end="")
    if calc_minutes == 1:
        return mins +" minute"
    elif calc_minutes >= 0:
       return mins +" minutes"


minutes_to_hours(60)
