def separate_words_by_start(words):
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_words = []
    consonant_words = []
    for word in words:
        if word and word[0] in vowels_list:
            vowel_words.append(word)
        else:
            consonant_words.append(word)
    return vowel_words, consonant_words

word_list = ["apple", "banana", "orange", "grape", "umbrella", "cat"]
v_words, c_words = separate_words_by_start(word_list)
print("Words starting with Vowels:", v_words)
print("Words starting with Consonants:", c_words)