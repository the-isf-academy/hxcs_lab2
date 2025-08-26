# /////////// INSTRUCTIONS /////////////////

# 🎲 Add randomness to your drawing! 

# ❓ Play with length, angle, pensize, circle, etc

# 🌈 Try to play with choosing a random color (take a look at file2.py)

# ////////////////////////////////////////////

# Don't delete this line! 
from turtle import *
from random import randint # this helps generate a random integer

# example use: this generates a random integer between 50 and 200
length = randint(50,200)
print(f"The random number is: {length}")

# This line makes the turtle go forward as long as "length"
forward(length)

# This line makes the program wait until the user types something on the keyboard
input("Type any key to close the program.")