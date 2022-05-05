def show_vowels(text):
    first_string = set(text.lower())
    second_string = set("aeiou")
    compare = first_string & second_string

    print("Vowels: " ,end="" )
    print(compare)


show_vowels("Umuzi")
