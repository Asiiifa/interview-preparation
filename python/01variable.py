# ==========================================
# Topic: Variables
# ==========================================

# Definition:
# A variable is a named memory location used to store data.

# Simple Definition:
# A variable is a container that stores a value.

# Purpose:
# - Store data
# - Reuse data
# - Update data
# - Make code readable

# Syntax:
# variable_name = value 
# Syntax:
# variable_name = value

#name = "Asifa"
#age = 29
#city = "Delhi"
#college = "ABC College"
#course = "B.Tech AI & ML" 

#📌 Interview Point

#Question: Can the value of a variable be changed?

#Answer:

#Yes. The value of a variable can be changed during program execution by assigning a new value to it.

name = "asifa"
print (name)

age = 24 

city = "delhi"
college = "its engineering college"
course = "btech"

print (age) 
print (college)
print (course)
print (city)

name = "asifa"

print(name)

name = "Ayesha"

print(name)

#📖 Interview Question

#Q: What is variable reassignment?

#A:

#Variable reassignment is assigning a new value to an existing variable.

city = "Delhi"
print(city)

city = "Mumbai"
print(city)

score = 50 
print (score)

score = 80 
print (score)

score = 100 
print (score)

# Interview Answer:
# A variable name must start with a letter or underscore,
# cannot start with a number, can contain letters,
# numbers and underscores, cannot contain spaces or
# special characters, and is case-sensitive.

# ==========================================
# Multiple Variable Assignment
# ==========================================

# Definition:
# Multiple Variable Assignment allows assigning
# values to multiple variables in a single line.

# Syntax:
# variable1, variable2 = value1, value2 

name, city, age, = "asifa" , "delhi" , 24

# ==========================================
# Interview Notes: Multiple Variable Assignment
# ==========================================

# Multiple Variable Assignment allows assigning
# values to multiple variables in a single line.

# The order of variables and values must match.

# Example:
# name, age, city = "Asifa", 24, "Delhi" 

# ==========================================
# Same Value to Multiple Variables
# ==========================================

# Definition:
# Python allows assigning the same value
# to multiple variables in a single statement.

# Syntax:
# variable1 = variable2 = variable3 = value

# Example:
# x = y = z = 100

a = b = c = "Python"

country = state = city = "India"

print(country)
print(state)
print(city)

# ==========================================
# Memory Concept
# ==========================================

# A variable stores a reference to a value
# in the computer's memory.

# Example:
# name = "Asifa"

# Memory:
# name -----> "Asifa"

# print(name) displays the value stored in memory.
name = "Asifa"

print(name)

# ==========================================
# Best Practices
# ==========================================

# 1. Use meaningful variable names.
# Example:
# student_name = "Asifa"

# 2. Follow snake_case naming convention.
# Example:
# total_marks = 450

# ==========================================
# Interview Questions - Variables
# ==========================================

# Q1. What is a Variable?
# A variable is a named memory location used to store data.

# Q2. Why do we use Variables?
# We use variables to store, reuse, and update data.

# Q3. What is the difference between a Variable and a Value?
# Variable -> Name used to store data.
# Value -> Actual data stored in the variable.

# Q4. What is the Assignment Operator?
# The assignment operator (=) assigns a value
# to a variable.

# Q5. Can a variable's value be changed?
# Yes. It is called Variable Reassignment. 

#assignment 
full_name = "asifa" 
age = 22
city = "newdelhi"
state = "delhi"
country = "india"
degree = "btech"
college = "its"
graduation_year = 2026
email = "asifakhan00279@gmail.com"
phone = 9005852549

print (full_name)
print (age)
print (city)
print (state)
print (country)
print (degree)
print (college)
print (graduation_year)
print (email)
print (phone) 

# ==========================================
# VARIABLES - CHEAT SHEET
# ==========================================

# Definition:
# A variable is a named memory location used to store data.

# Syntax:
# variable_name = value

# Example:
# name = "Asifa"
# age = 22

# Assignment Operator:
# =

# Print:
# print(variable_name)

# Multiple Variable Assignment:
# x, y = 10, 20

# Same Value Assignment:
# a = b = c = 100

# Reassignment:
# age = 22
# age = 23

# Naming Rules:
# ✅ Start with letter or underscore (_)
# ✅ Can contain letters, numbers and underscores
# ❌ Cannot start with number
# ❌ No spaces
# ❌ No special characters

# Best Practice:
# Use meaningful names.
# Follow snake_case.

# Example:
# student_name = "Asifa"