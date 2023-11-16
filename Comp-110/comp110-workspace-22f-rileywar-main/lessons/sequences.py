"""Examples of the tuple and range sequences"""

# An example of a tuple without aliasing
goat: tuple[str, int] = ("MJ", 23)

# tuples are sequences, so they're 0 indexed
print(goat[0])
print(goat[1])

# Printing a tuple produces its lliteral syntax
print(goat)

# Print both items on the same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences hav lenghts
print(len(goat))

# Sequences are iterable with for..in loops
# Meaning you can loop them with for..in
for item in goat:
    print(item)

# tuples, unlike lists, are immutable
# cannot reassign items, or append, or pop
# goat[0] = "LBJ" does not work


# We can invent our own type with a type alias
Player = tuple[str, int]

# Once we invent a type, we cam create variable of that type
unc_poy: Player = ("Bacot", 5)

# In a strange world where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)


# A rage is another common sequence type
zero_to_nine: range = range(0, 10, 1)

# We can access items
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# we can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)

names: list[str] = ["Kris", "Mason", "Riley", "Chris"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")


print(odds_to_99.stop)