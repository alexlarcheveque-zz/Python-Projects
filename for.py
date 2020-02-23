vowels = 0
consonants = 0

word = input("Please enter a sentence/word for us: ")

for letter in word:
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter == " ":
        pass
    else:
        consonants += 1

print("vowels: ", vowels)
print("consonants: ", consonants)
