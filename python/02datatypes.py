# ==========================================
# Topic: Data Types
# ==========================================

# Definition:
# A data type defines the type of data
# that a variable can store.

# Examples:
# "Asifa" -> String (str)
# 22 -> Integer (int)
# 99.5 -> Float (float)
# True -> Boolean (bool)
# ==========================================
# Why Do We Need Data Types?
# ==========================================

# Data types help Python understand
# what kind of data is stored
# in a variable.

# Example:
# "Asifa" -> Text
# 22 -> Number
# True -> Boolean

# ==========================================
# Built-in Data Types
# ==========================================

# Python provides built-in data types
# to store different kinds of data.

# str   -> String (Text)
# int   -> Integer (Whole Numbers)
# float -> Decimal Numbers
# bool  -> Boolean (True or False)

# ==========================================
# type() Function
# ==========================================

# Definition:
# The type() function is used to find
# the data type of a variable or value.

# Syntax:
# type(variable_name)
# type(value)

name = "Asifa"

print(type(name))

age = 22

print(type(age))


name = "Asifa"
age = 22
marks = 89.5
is_student = True

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student)) 

# ==========================================
# String (str)
# ==========================================

# Definition:
# A string is a sequence of characters
# enclosed in single or double quotes.

# Quotes tell Python that the value is text,
# not a variable name.

# ==========================================
# Valid and Invalid Strings
# ==========================================

# Valid Strings:
# city = "Delhi"
# country = 'India'
# language = "Python"

# Invalid Strings:
# city = Delhi
# language = "Python

# Why Invalid?
# 1. Missing quotes
# 2. Missing closing quote

# Common Errors:
# NameError
# SyntaxError

# Interview Question:
# Q. What makes a string invalid?
# A. A string becomes invalid if it is not
#    enclosed properly in quotes or if the
#    closing quote is missing.

# ==========================================
# Strings with Numbers
# ==========================================

# Numbers inside quotes are still Strings.

# Examples:
# phone = "9876543210"
# pin = "1234"
# password = "abc123"
# address = "House No. 25"

# Without Quotes:
# phone = 9876543210

# Data Type:
# "9876543210" -> str
# 9876543210 -> int

# Important Rule:
# Quotes change the data type.

# Interview Question:
# Q. Is "12345" an integer?
# A. No. It is a string because it is enclosed
#    in quotes. 

# ==========================================
# String Concatenation
# ==========================================

# Definition:
# Concatenation means joining two or more
# strings using the (+) operator.

# Syntax:
# string1 + string2

# Example:
# first_name = "Asifa"
# last_name = "Khan"

# full_name = first_name + last_name

# Output:
# AsifaKhan

# To add a space:
# full_name = first_name + " " + last_name

# Output:
# Asifa Khan

# Python does NOT add spaces automatically.

# Example:
# "AI" + "ML"
# Output: AIML

# "AI" + " " + "ML"
# Output: AI ML

# "AI" + "-" + "ML"
# Output: AI-ML

# Interview Question:
# Q. What is string concatenation?
# A. String concatenation is the process of
#    joining two or more strings using the
#    (+) operator. 

# ==========================================
# Practice Questions
# ==========================================

# Q1. Create a variable called name and store your name.
#
# Q2. Create a variable called city and store your city name.
#
# Q3. Create a variable called college and print its data type.
#
# Q4. Store your phone number as a string and print its data type.
#
# Q5. Create first_name and last_name variables and join them using (+).
#
# Q6. Print your full name with a space between first name and last name.
#
# Q7. Print the output:
# Hello Asifa!
# (Replace Asifa with your own name.)
#
# Q8. Predict the output:
#
# language = "Python"
# version = "3.12"
#
# print(language + version)
#
# Q9. Predict the output:
#
# language = "Python"
# version = "3.12"
#
# print(language + " " + version)
#
# Q10. What is the data type of:
#
# "500"
# 500
# "True"
# True
first_name = "Asifa"
last_name = "Khan"

full_name = first_name + last_name

print(full_name)

first_name = "Asifa"
last_name = "Khan"

full_name = first_name + " " + last_name

print(full_name)

city = "New"
country = "Delhi"

print(city + " " + country)

name = "Asifa"

print("Hello " + name + "!")

# ==========================================
# Difference Between + and ,
# ==========================================

# (+) joins strings together.
#
# (,) prints multiple values and automatically
# adds a space between them.
#
# Examples:
#
# print("AI" + "ML")
# Output:
# AIML
#
# print("AI", "ML")
# Output:
# AI ML
#
# print("City:" + "Delhi")
# Output:
# City:Delhi
#
# print("City:", "Delhi")
# Output:
# City: Delhi
#
# Interview Question:
# Q. What is the difference between (+) and (,)
# in the print() function?
#
# A.
# (+) is used to concatenate (join) strings.
# (,) prints multiple values and automatically
# inserts a space between them.

print("Hello" + "Python")

name = "Asifa"

print("Hello", name)

name = "Asifa"

print("Hello " + name)

# ==========================================
# Integer (int)
# ==========================================

# Definition:
# An integer is a whole number without
# a decimal point.

# Examples:
# age = 22
# marks = 95
# temperature = -10
# score = 0

# Invalid Integer Example:
# price = 99.5

# Data Types:
# 22 -> int
# -10 -> int
# 0 -> int
# 99.5 -> float

# Interview Question:
# Q. What is an integer?
#
# A. An integer is a whole number without
# a decimal point.

# ==========================================
# Float (float)
# ==========================================

# Definition:
# A float is a number that contains
# a decimal point.

# Examples:
# price = 99.99
# temperature = 36.5
# discount = 0.25
# balance = -100.75

# Data Types:
# 99.99 -> float
# 36.5 -> float
# 0.25 -> float
# -100.75 -> float

# Not Float:
# 22 -> int

# Interview Question:
# Q. What is a float?
#
# A. A float is a number that contains
# a decimal point.