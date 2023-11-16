"""EX06 Choose Your Own Adventure."""

__author__ = str(730579921)

points: int = 0
player: str = ""
mon_name: str = ""
mon_health: int = 100
health_tracker: int = 0
SMILEY_FACE: str = "\U0001F600"

from random import randint


def main() -> None:
    """The main function of the program."""
    print(greet())
    while points >= 0:
        print(f"Adventure points: {points}")
        where_to: str = input(f"Where to next?\nPlease enter 1, 2, or 3\n1. Find a battle\n2. Feed your Krismon\n3. Stop playing\n")
        if where_to == "1":
            print(battle())
        if where_to == "2": 
            print(feed(points))
        if where_to == "3": 
            print(f"Thanks for playing, {player}, Have a good day!\nAdventure points: {points}")
            exit()
        while where_to != ("1") and where_to != ("2") and where_to != ("3"):
            where_to: str = input("That wasn't a 1, 2, or 3! Try again: ")

def battle() -> None:
    """The battle sequence of the Krismon game."""
    turn_count: int = 1
    opponent_damage: int = 0
    opponent_health: int = 100
    mon_health: int = 100
    mon_damage: int = 0
    attack_or_defend: str = ""
    global mon_name
    mon_name = input("Please name your Krismon. ")
    print(f"It's time to battle, {mon_name}! Get ready!")
    print("Your opponent is Autograder!!!")


    while opponent_health > 0 and mon_health > 0:
        print(f"--Turn {turn_count}--")
        attack_or_defend: str = input("Press 1 to attack, Press 2 to defend: ")
        if attack_or_defend == "1":
            mon_damage += randint(1, 20)
            opponent_damage += randint(1, 20)
            opponent_health -= mon_damage
            mon_health -= opponent_damage
            global health_tracker
            health_tracker = mon_health
            print(f"Your attack did {mon_damage} damage! Opponent has {opponent_health} hp left.")
            print(f"Opponents attack did {opponent_damage} damage! {mon_name} has {mon_health} hp left.")
            opponent_damage = 0
            mon_damage = 0
            turn_count += 1
            global points
            points += 1
        if attack_or_defend == "2":
            print("Opponents next attack skipped. ")
            turn_count += 1
    if opponent_health <= 0 and mon_health >= 0:
        return("Congrats, you won!")
    if opponent_health >= 0 and mon_health <= 0:
        return("Sorry, you lost. :(")
    else:
        return("Looks like a draw. Try Again!")

def feed(amount: list[int]) -> int:
    if amount == 0:
        return("You have 0 points! You should go battle first.")
    global points
    points += 1
    return(f"You fed your krismon {amount} treats! Now they love you even more :)")

def greet() -> None:
    """Prints a welcome message and asks for the user's name."""
    global player
    player = input("What is your name? ")
    return(f"Welcome to Krismon, {player}! Krismon is a pokemon style fighting game. Have fun! {SMILEY_FACE}")



if __name__ == "__main__":
  main()