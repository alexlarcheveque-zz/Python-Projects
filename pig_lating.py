#user input sentence

orginal = input("Please enter a setence: ").strip().lower()

#split words into array

words = orginal.split()

#loop through array and convert to pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        beg_seg = word[:vowel_pos]
        new_words.append(word[vowel_pos:] + beg_seg + "yay")
print(" ".join(new_words))
