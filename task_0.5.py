def area_triangle_calc(side_one, side_two, side_three):
    half_perimeter = (side_one + side_two + side_three) / 2
    area_calc = (half_perimeter * (half_perimeter - side_one) * (half_perimeter - side_two) * (half_perimeter - side_three) ) ** 0.5
    return




area_triangle_calc(5,6,7)
