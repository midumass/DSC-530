# -*- coding: utf-8 -*-
"""
DSC530-T302 Assignment 1.4
Zachary Hill
09JUN2019

Using Python, submit your results via your notebook or export your code and submit via the assignment link. You must show your code to get full credit. 

Display the text “Hello World! I wonder why that is always the default coding text to start with”
Add two numbers together
Subtract a number from another number
Multiply two numbers
Divide between two numbers
Concatenate two strings together (any words)
Create a list of 4 items (can be strings, numbers, both)
Append an item to your list (again, can be a string, number)
Create a tuple with 4 items (can be strings, numbers, both)
"""

# Variables defined globally to be called for each step of the assignment
x1 = 2
x2 = 1

# Display the text “Hello World! I wonder why that is always the default coding text to start with”
print("Hello World! I wonder why that is always the default coding text to start with")

# Add two numbers together
print("Using mathematical figures and operators as parameters")
print (2 + 1)

print("Calling a variable with a previously calculated value as a parameter")
x3 = x1 + x2
print(x3)

# Subtract a number from another number
print("Using mathematical figures and operators as parameters")
print (2 - 1)

print("Calling a variable with a previously calculated value as a parameter")
x4 = x1 - x2
print(x4)

# Multiply two numbers
print("Using mathematical figures and operators as parameters")
print (2 * 1)

print("Calling a variable with a previously calculated value as a parameter")
x5 = x1 * x2
print(x5)

# Divide between two numbers
print("Using mathematical figures and operators as parameters")
print (2 / 1)

print("Calling a variable with a previously calculated value as a parameter")
x6 = x1 / x2
print(x6)

# Concatenate two strings together (any words)
word1 = "any"
word2 = "words"
print(word1 + word2)

# Create a list of 4 items (can be strings, numbers, both)
list1 = [x1, x2, word1, word2]
print(list1)

# Append an item to your list (again, can be a string, number)
list1.append("an item")
print(list1)

# Create a tuple with 4 items (can be strings, numbers, both)
tuple1 = (x1, x2, word1, word2)
print(tuple1)