'''
Name: Mr. Smith
Date: 2/14/25
Description: Unit 1 Lesson 3 - Dictionaries Part 2. 
Covers more about accessing items (especially if a key is not present), modifying dictionary items,
removing key-value pairs, 
'''

contacts = { "Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278 }

print()
print("Method 1".center(20,"-"))
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
print("Method 2".center(20,"-"))
# Retrieval method 2
print(f"Fred's number is {contacts.get("Fred")}")
print(f"John's number is {contacts.get("John")}")
print(f"John's number is {contacts.get("John",411)}")
print(contacts)
