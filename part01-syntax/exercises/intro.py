#using input function
user_input_name = input("what is your name?")
user_input_age = input("how old are you?")
# converting to int
age = int(user_input_age)
user_input_height = input("what is your height in meters?")
# converting to float
height = float(user_input_height)
# using variables and calling them
print(f"My name is {user_input_name}, I am {age} years old, and I am {height}m tall.")
# operator
future_age = age + 10
#printing
print(future_age)