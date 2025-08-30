# 💻 Code Example
# print("Hello, World!")
# 👉 Output:
# Hello, World!

# 🏋️ Exercises
# 1. Print your name.
# 2. Print your favorite quote.
# 3. Print: I am learning Python with Alkoders!.

# SOLUTIONS
# 1. Print your name
print("Ali")
# 2. Print your favorite quote
print("Talk is cheap. Show me the code.- Linus Torvalds")
# 3. Print learning message
print("I am learning Python with Alkoders!")

# 💻 Code Example
# name = "Ali" # String
# age = 20 # Integer
# pi = 3.14 # Float
# is_student = True # Boolean
# print(name, age, pi, is_student)
# 👉 Output:
# Ali 20 3.14 True

# 🏋️ Exercises
# 1. Create variables for your name, age, and city and print them.
# 2. Store the value of 10 / 3 in a variable and print it rounded to 2 decimals.
# 3. Assign values to x = 5, y = 2.5 and print their sum, product, and type

# ✅ Solutions
# # 1. Variables for name, age, city
# name = "Ali"
# age = 21
# city = "Karachi"
# print("My name is", name,"I am", age,"years old and I live in",city)
# # 2. Division with rounding
# result = 10 / 3
# print(round(result, 2)) # 3.33
# # 3. Mixed data types
# x = 5
# y = 2.5
# print("Sum:"
# , x + y)
# print("Product:"
# , x * y)
# print("Type of x:"
# , type(x))
# print("Type of y:"
# , type(y))

# 💻 Code Example
# name = input("Enter your name: ")
# print("Hello,
# "
# , name)
# age = int(input("Enter your age: "))
# print("Next year, you will be"
# , age + 1)
# 👉 Output (example):
# Enter your name: Ali
# Hello, Ali
# Enter your age: 20
# Next year, you will be 21

# 🏋️ Exercises
# 1. Take two numbers from the user and print their sum.
# 2. Ask the user’s age and print: "You will be X years old after 10 years.
# "
# 3. Take a string input and print it in uppercase.

# ✅ Solutions
# # 1. Sum of two numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Sum is:"
# , num1 + num2)
# # 2. Age after 10 years
# age = int(input("Enter your age: "))
# print("You will be"
# , age + 10,
# "years old after 10 years.
# ")
# # 3. Uppercase string
# text = input("Enter something: ")
# print("Uppercase:"
# , text.upper())

# 💻 Code Example
# x, y = 10, 3
# print("Addition:"
# , x + y)
# print("Subtraction:"
# , x - y)
# print("Multiplication:"
# , x * y)
# print("Division:"
# , x / y)
# print("Floor Division:"
# , x // y)
# print("Power:"
# , x ** y)
# 👉 Output:
# Addition: 13
# Subtraction: 7
# Multiplication: 30
# Division: 3.3333...
# Floor Division: 3
# Power: 1000

# 🏋️ Exercises
# 1. Write a program to calculate the area of a rectangle.
# 2. Check if a number is even or odd.
# 3. Compare two numbers and print which one is greater.

# ✅ Solutions
# # 1. Area of rectangle
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# print("Area =
# "
# , length * width)
# # 2. Even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
# print("Even")
# else:
# print("Odd")
# # 3. Greater number
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
# print(a,
# "is greater")
# elif b > a:
# print(b,
# "is greater")
# else:
# print("Both are equal")

# 💻 Code Example
# age = int(input("Enter your age: "))
# if age >= 18:
# print("You are an Adult")
# elif age == 17:
# print("Almost there!")
# else:
# print("You are a Minor")
# 👉 Output (for age=20):
# You are an Adult

# 🏋️ Exercises
# 1. Write a program that checks if a number is positive, negative, or zero.
# 2. Take marks input and print grades:
# ○
# >= 80 → Grade A
# ○
# >= 60 → Grade B
# ○
# else → Fail
# 3. Ask the user for their age and print whether they are a child (<13), teenager (13–19), or
# adult (20+).

# ✅ Solutions
# # 1. Positive/Negative/Zero
# num = int(input("Enter a number: "))
# if num > 0:
# print("Positive")
# elif num < 0:
# print("Negative")
# else:
# print("Zero")
# # 2. Grading system
# marks = int(input("Enter marks: "))
# if marks >= 80:
# print("Grade A")
# elif marks >= 60:
# print("Grade B")
# else:
# print("Fail")
# # 3. Age classification
# age = int(input("Enter your age: "))
# if age < 13:
# print("Child")
# elif age <= 19:
# print("Teenager")
# else:
# print("Adult")

# 💻 Code Example
# # For loop
# for i in range(1, 6):
# print("For loop iteration:"
# , i)
# # While loop
# count = 1
# while count <= 5:
# print("While loop iteration:"
# , count)
# count += 1
# # Break and continue
# for i in range(1, 6):
# if i == 3:
# continue # skip 3
# if i == 5:
# break # stop at 5
# print(i)

# 🏋️ Exercises
# 1. Print all numbers from 1 to 100.
# 2. Print the multiplication table of a number given by the user.
# 3. Calculate the sum of numbers from 1 to N (user input).
# 4. Print only even numbers from 1 to 50.

# ✅ Solutions
# # 1. Numbers 1 to 100
# for i in range(1, 101):
# print(i)
# # 2. Multiplication table
# n = int(input("Enter number: "))
# for i in range(1, 11):
# print(n,
# "x"
# , i,
# "
# =
# "
# , n * i)
# # 3. Sum of 1 to N
# n = int(input("Enter number: "))
# total = 0
# for i in range(1, n + 1):
# total += i
# print("Sum =
# "
# , total)
# # 4. Even numbers
# for i in range(2, 51, 2):
# print(i)

# 💻 Code Example
# # List
# fruits = ["apple"
# ,
# "banana"
# ,
# "mango"]
# print(fruits[0]) # apple
# fruits.append("orange")
# print(fruits)
# # Tuple
# coords = (10, 20)
# print(coords[1]) # 20

# 🏋️ Exercises
# 1. Make a list of 5 favorite movies and print them one by one.
# 2. Create a tuple of 3 numbers and calculate their sum.
# 3. Remove "banana" from the list: ["apple"
# ,
# "banana"
# ,
# "mango"].

# ✅ Solutions
# # 1. Movies list
# movies = ["Inception"
# ,
# "Titanic"
# ,
# "Avengers"
# ,
# "Interstellar"
# ,
# "Batman"]
# for movie in movies:
# print(movie)
# # 2. Tuple sum
# nums = (5, 10, 15)
# print("Sum =
# "
# , sum(nums))
# # 3. Removing banana
# fruits = ["apple"
# ,
# "banana"
# ,
# "mango"]
# fruits.remove("banana")
# print(fruits)

# 💻 Code Example
# student = {
# "name": "Ali"
# ,
# "age": 20,
# "grade": "A"
# }
# print(student["name"])
# student["age"] = 21
# print(student)

# 🏋️ Exercises
# 1. Create a dictionary with name, age, city and print values.
# 2. Update the dictionary to add "country": "Pakistan"
# .
# 3. Create a dictionary of 3 students and their marks, then print them.

# ✅ Solutions
# # 1. Basic dictionary
# person = {"name": "Ali"
# ,
# "age": 20,
# "city": "Karachi"}
# print(person["name"], person["age"], person["city"])
# # 2. Adding new key
# person["country"] =
# "Pakistan"
# print(person)
# # 3. Students dictionary
# marks = {"Ali": 85,
# "Sara": 92,
# "Ahmed": 78}
# for student, score in marks.items():
# print(student,
# "scored"
# , score)

# Examples
# def greet(name):
# print("Hello,
# "
# , name)
# def add(a, b):
# return a + b
# greet("Ali")
# print(add(5, 3))

# Exercises
# 1. Create a function square(n) → returns n²
# .
# 2. Write a function to calculate the sum of two numbers.
# 3. Write a function to find the factorial of a number.

# Solutions
# def square(n):
# return n * n
# print(square(4))
# def add(a, b):
# return a + b
# print(add(10, 7))
# def factorial(n):
# fact = 1
# for i in range(1, n+1):
# fact *= i
# return fact
# print(factorial(5))

# Examples
# # Writing to a file
# with open("hello.txt"
# ,
# "w") as f:
# f.write("Hello, Python!\n")
# # Reading from a file
# with open("hello.txt"
# ,
# "r") as f:
# content = f.read()
# print(content)