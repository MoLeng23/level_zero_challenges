def common_letters(string_one, string_two):
    set_one = set(string_one.lower())
    set_two = set(string_two.lower())

    letter = set_one & set_two
    print("Common letters: " )
    print(letter)


common_letters("house","computers")

