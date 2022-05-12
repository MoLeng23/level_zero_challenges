def show_vowels(text_one,text_two):
    text_one = set(text_one.lower())
    text_two = set(text_two.lower())
     
    print("Common letters: ", end="")
    sep = "%s"
    for letter in text_one and text_two:
        if letter in text_one and text_two:
            print(sep % letter, end="" )
            sep = ",%s"


show_vowels("hooouse", "comoooputers")

