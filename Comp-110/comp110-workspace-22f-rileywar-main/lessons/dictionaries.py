"""Demonstrations of dictionary capabilities"""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to any empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")


# Update / reassign a key value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Cannot have duplicate keys
# Can have duplicate values

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} # Same as dict()

# Alternatively, initialize hey value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)


# Acess a key that doesn't exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")