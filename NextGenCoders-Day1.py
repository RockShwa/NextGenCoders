# This is a comment

# Activity 1 - Print Statement
print("Hello World")



# Activity 2 - Tell Us About Yourself!
# Name
# Favorite Color
# Favorite Animal
# Something you're looking forward to
# A question about Python or programming

print("My name is Aubrey, but some people call me Bee!")
print("My favorite color is purple")
print("My favorite animal is an otter")
print("I'm looking forward to teaching Python")
print("What are the main differences between Python and other programming languages?")



# Activity 3 - Making Variables
# A variable is like a container with a label, it's a place to store things
name = "Aubrey" # string (you can think of as text)
lucky_number = 7 # numbers



# Activity 4 - User Input
favorite_food = input("What is your favorite food? ")
print(favorite_food)

# You can combine the user input in a sentence using +
print("Your favorite food is " + favorite_food + "!")



# Activity 5 - Estimated Age
# Get the user's birth year
# Calculate their estimated age (so if this year is 2025, and I was born in 2008, how old am I?)
# Print the estimated age along with a summary

birth_year = input("What is the year you were born? ")
# The int() function converts the birth year from a string (text) to a number
age = 2025 - int(birth_year)
# The str() function converts the age from a number to a string (text)
print("Your estimated age is " + str(age) + " years old!")



# Activity 6 - Mad Libs!
# The challenge:
# Adjectives, nouns, verbs
# Make a story!

noun_1 = input("Noun: ")
noun_2 = input("Noun: ")
verb_1 = input("Verb: ")

print("I watched a " + noun_1 + " with my friend " + noun_2 + " who loves to " + verb_1 + ".")
