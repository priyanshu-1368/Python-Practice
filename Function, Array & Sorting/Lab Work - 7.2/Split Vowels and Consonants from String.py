def split_vowels_consonants(text):
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = ""
    others = ""
    for char in text:
        if char in vowels_list:
            vowels += char
        else:
            others += char
    return vowels, others

v, o = split_vowels_consonants("Programming")
print("Vowels:", v)
print("Remaining:", o)