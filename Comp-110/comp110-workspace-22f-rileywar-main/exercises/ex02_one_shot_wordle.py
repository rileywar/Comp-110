"""EX02 One Shot Wordle."""

__author__ = str(730579921)

secret: str = ("python")
word_choice: str = input(f"What is your { len(secret) }-letter guess? ")
word_index: str = word_choice[0]
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
i: int = 0
exist: bool = False
alternate: int = 0

while len(word_choice) != len(secret):
    word_choice = input(f"That was not { len(secret) } letters! Try again:")

while i < len(secret):
    if word_choice[i] == secret[i]:
        emoji += GREEN_BOX
    else:
        while alternate < len(secret):
            if word_choice[i] == secret[alternate]:
                exist = True
            alternate += 1
        if exist is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1
    exist = False
    alternate = 0

print(emoji)

if word_choice != secret:
    print("Not quite. Play again soon!")

if word_choice == secret:
    print("Woo! You got it!")
