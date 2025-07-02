# NextGenCoders: Welcome to Day 2!

# Today we're talking about logic
# - Comparison Operators
# - If Statements
# - For Loops
# - While Loops

# If Statements
user_num = input("Choose a number: ")

if user_num == "2":
    print("Hello World")
else:
    print("Bye World")   
    
# While Loop
x = 1

while x < 10:
    print("hi")
    x+=1
    print(x)
    
# For Loop

for i in range(5):
    print("Hello World!")    
    
# Activity One - Yes/No Quiz
answer_1 = input("Do you like cabbage? ")

if (answer_1 == "yes" or answer_1 == "Yes"):
    print("cool, me too!")
else:
    print("aww that's sad")    
    
answer_2 = input("Do you think beaches are better than the mountains? ")    

if (answer_1 == "yes" or answer_1 == "Yes"):
    print("aww that's sad")
else:
    print("mountains are better :D")  
    
# Activity Two - Custom Age Message

age = int(input("How old are you? "))

if (age < 12):
    print("you're not a teenager yet!")
elif (age == 12):
    print("congrats, you're a teenager!")
else:
    print("you're old!")    
    
# Activity 3 - Name Repeater
for i in range(10):
    print("My name is Aubrey")

# Activity 4 - Count to 10
for i in range(10):
    print(i + 1)

# Activity 5
user_input = "no"
while user_input == "No" or user_input == "no":
    user_input = input("Do you want to stop? ")


# Make a List!

shopping_list = ["dates", "matcha", "bell peppers", "carrots", "hummus"]

for item in shopping_list:
    print(item)
    
# Function
def say_hello():
    print("Hi Everyone!")
    
say_hello()   
    
    
