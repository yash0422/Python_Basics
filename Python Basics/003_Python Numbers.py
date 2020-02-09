# PYTHON NUMBERS

# There are three numeric types in Python:
   # int
   # float
   # complex
# Variables of numeric types are created when you assign a value to them:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function:

# Example
print(type(x))
print(type(y))
print(type(z))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# RANDOM NUMBERS

# Python does not have a random() function to make a random number, but Python has a built-in module called
# random that can be used to make random numbers:
# Import the random module, and display a random number between 1 and 9:

import random
print(random.randrange(10,20))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# TYPE CONVERSION

# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1                                                   # int
y = 2.8                                                 # float
z = 1j                                                  # complex

# this will convert [ (x = 1) to 1.0 ] from int to float:
a = float(x)

# this will convert [ (y = 2.8) to 2 ] convert from float to int:
b = int(y)

# this will convert [ (x = 1 to (1+0j) ] from int to complex:
c = complex(x)

print(a)                                                # ans = 1.0
print(b)                                                # ans = 2
print(c)                                                # ans = (1+0j)

print(type(a))
print(type(b))
print(type(c))

# # # Note: You cannot convert complex numbers into another number type. # # #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
