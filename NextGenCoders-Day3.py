import turtle
import math

# NextGenCoders: Welcome to Day 3

# Today we're learning about:
# 1. Python Math
# 2. Python Turtle Graphics

# Activity 1 - 4 Function Calculator
'''
Step 1: Make 4 functions (remember def from yesterday!) that perform addition, subtraction, multiplication and division.
(Hint: add(a, b), subtract(a, b), divide(a, b), multiply(a, b))
Step 2: Ask the user for an operation: +, -, /, or *
Step 3: Ask the user for 2 numbers
Step 4: Use if/elif statements to call the right function based on the operation entered
Step 5: Print the result of the operation
'''

# Step 1

def add(a, b):
    print(int(a) + int(b))
    
def subtract(a, b):
    print(int(a) - int(b))
    
def divide(a, b):
    print(int(a) / int(b))
    
def multiply(a, b):
    print(int(a) * int(b))            



user_operation = ""

while user_operation != "stop" or user_operation != "Stop":
    # Step 2
    user_operation = input("What operation would you like to perform (+, -, /, *), or type stop to quit: ")
    if (user_operation == "stop" or user_operation == "Stop"):
        break

    # Step 3
    user_num_1 = input("Enter a number: ")
    user_num_2 = input("Enter a number: ")

    # Step 4
    if user_operation == "+":
        add(user_num_1, user_num_2)
    elif user_operation == "-":
        subtract(user_num_1, user_num_2)
    elif user_operation == "/":
        divide(user_num_1, user_num_2)
    elif user_operation == "*":
        multiply(user_num_1, user_num_2)       
    else:
        print("That's not a valid operation!")    
        
# Python Turtle
    
# Fullscreen the Canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Start
t = turtle.Turtle()
t.shape("turtle")

t.pendown()
t.forward(100)
t.dot(100, "purple")

screen.exitonclick()
        
        
        
