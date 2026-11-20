text = input("Enter a sentence: ")

frequency = {}

for character in text.lower():

    if character.isalpha():

        if character in frequency:
            frequency[character] += 1

        else:
            frequency[character] = 1

print("\nCHARACTER FREQUENCY")

for character, count in sorted(frequency.items()):

    print(character, ":", count)