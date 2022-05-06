def minutes_to_hours(minutes):
    calc_hours = minutes // 60
    calc_minutes = minutes % 60
    if calc_hours == 1:
        print(str(calc_hours) +" hour", ",", " ", end="")
    elif calc_hours > 1:
        print(str(calc_hours) +" hours", ",", " ", end="")
    elif calc_hours == 0:
        print(str(calc_hours) + " hours", "," , " ", end="")
    if calc_minutes == 1:
        print(str(calc_minutes) +" minute")
    elif calc_minutes > 1:
        print( str(calc_minutes) +" minutes")
    elif calc_minutes == 0:
        print(str(calc_minutes) + " minutes" )




minutes_to_hours(000)

