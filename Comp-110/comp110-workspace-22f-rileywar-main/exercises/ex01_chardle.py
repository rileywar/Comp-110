"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = str(730579921)

word_choice: str = input("Please enter a 5 character word:")
if len(word_choice) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character_choice: str = input("Please enter a single character:")
if len(character_choice) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character_choice + " in " + word_choice)

count: int = 0

if character_choice == word_choice[0]:
    print(character_choice + " found at index 0") 
    count = count + 1

if character_choice == word_choice[1]:
    print(character_choice + " found at index 1")
    count = count + 1

if character_choice == word_choice[2]:
    print(character_choice + " found at index 2")
    count = count + 1

if character_choice == word_choice[3]:
    print(character_choice + " found at index 3")
    count = count + 1

if character_choice == word_choice[4]:
    print(character_choice + " found at index 4")
    count = count + 1

if count == 1:
    print("1 instance of " + character_choice + " found in " + word_choice)
else:
    if count == 0:
        print("No instances of " + character_choice + " found in " + word_choice)
    else:
        if count > 1:
            print((str(count) + " instances of " + character_choice + " found in " + word_choice))