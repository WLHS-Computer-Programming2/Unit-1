"""
Name: Mr. Smith
Date: 2-9-25
Unit: 1
Topic: List Comprehensions
"""

# List comprehensions

# old way
evens_list1 = []
for i in range(1, 11):
    evens_list1.append(i**2)
print(evens_list1)

# list comprehension way
evens_list2 = [i**2 for i in range(1, 11)]
print(evens_list2)


# List comprehensions with conditionals
