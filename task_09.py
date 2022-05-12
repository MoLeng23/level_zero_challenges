def show_vowels(text):
    text = text.lower()
    print("vowels: ", end="")
    sep = "%s"
    for vowel in "aeiou":
        if vowel in text:
            print(sep % vowel, end="")
            sep= ", %s"
      


show_vowels("Umuzi")
