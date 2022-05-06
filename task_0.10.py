def show_vowels(text_one,text_two):
    text_one = text_one.lower()
    text_two = text_two.lower()

    print("Common letters: ", end="")

    for letter in text_one and text_two:
        if letter in text_one and text_two:
            print(letter, end="," )
   


show_vowels("house", "computers")
