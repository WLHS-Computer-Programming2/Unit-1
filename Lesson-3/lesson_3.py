"""
Name: Mr. Smith
Date: 2/14/25
Description: Unit 1 Lesson 3 - Dictionaries Part 2. 
Covers more about accessing items (especially if a key is not present), modifying dictionary items,
removing key-value pairs, 
"""

contacts = {"Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278}

print()
print("Method 1".center(20, "-"))
# Retrieval method 1
print(f"Fred's number is {contacts["Fred"]}")

if "John" in contacts:
    print(f"John's number is {contacts["John"]} ")
else:
    print("John is not in the contact list")

try:
    print(f"John's number is {contacts["John"]} ")
except KeyError:
    print("John is not in the contact list")

print()
print("Method 2".center(20, "-"))
# Retrieval method 2
print(f"Fred's number is {contacts.get("Fred")}")
print(f"John's number is {contacts.get("John")}")
print(f"John's number is {contacts.get("John",411)}")
print(contacts)


# starting with empty dictionary
print()
print("Modifying Lists".center(20, "-"))
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
alien_0["color"] = "yellow"
print(alien_0)
print(f"The alien's color is {alien_0['color']}")

alien_0["x-pos"] = 0
alien_0["y-pos"] = 25
alien_0["speed"] = "medium"

####
# If the speed is slow, increment x_pos by 1. If medium, by 2
# If fast, by 3. Print the initial position and the new position
####
print(f"Original position: {alien_0['x-pos']}")
if alien_0["speed"] == "slow":
    alien_0["x-pos"] += 1
elif alien_0["speed"] == "medium":
    alien_0["x-pos"] += 2
elif alien_0["speed"] == "fast":
    alien_0["x-pos"] += 3
else:
    print("Invalid speed")

print(f"New position: {alien_0['x-pos']}")

# removing key-value pairs
alien_0["home planet"] = "Neptune"
print(alien_0)

del alien_0["home planet"]
print(alien_0)

## Formatting dictionaries - one key/value pair per line
alien_1 = {
    "color": "blue", 
    "points": 10, 
    "x-pos": 50, 
    "y-pos": 30, 
    "speed": "fast"
}
