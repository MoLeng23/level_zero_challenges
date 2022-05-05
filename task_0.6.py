def maximum(num_one, num_two, num_three):

    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three and num_two > num_one:
        return num_two
    else:
        return num_three

maximum(1,2,3)

