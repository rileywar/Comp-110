"""EX03 Structured Wordle."""

__author__ = str(730579921)
index: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret: str, char: str) -> bool: 
    """Checks if char is located at any index of search."""
    index: int = 0
    assert len(char) == 1
    while index < len(secret):
        if char == secret[index]:
            return True
        index += 1
    return False
       

def emojified(guess: str, secret: str) -> str: 
    """Returns a string of emoji boxes based on the users guess."""
    emojis: str = ""
    index: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    while index < len(secret):
        if guess[index] == secret[index]:
            emojis += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        index += 1
    return emojis 


def input_guess(expected: int) -> str: 
    """Prompts the user for a guess."""
    guess: str = input(f"Enter a {expected} character word: ")
    while len(guess) != (expected):
        guess = input(f"That wasn't {expected} chars! Try again: ")
    return guess


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "string"
    i: int = 1
    expected: int = len(secret)
    win: bool = False
    
    while i <= 6 and win is False:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(expected)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {i}/6 turns!")
            win = True
        i += 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__": 
    main()