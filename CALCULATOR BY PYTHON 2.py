#!/usr/bin/env python
# coding: utf-8

# # A simple calculator in Python

# Python as a calculator
# Python is perfectly suited to do basic calculations. It can do addition, subtraction, multiplication and division.

# In[1]:




# Define the function for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Display the menu options
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation based on user choice using if, elif statement
if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Invalid input")

