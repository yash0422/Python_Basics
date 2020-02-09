# PYTHON VARIABLES

# Create a Variable
x = 5
y = "John"
print(x)                        # ans = 5
print(y)                        # ans = John

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Output both text and a variable
x = "awesome"
print("Python is " + x)         # ans = Python is awesome

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# add a variable to another variable
x = "Python is "
y = "awesome"
z = x + y
print(z)                        # ans = Python is awesome

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4                           # x is of type int
x = "Sally"                     # x is now of type str
print(x)                        # ans = Sally

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# String variables can be declared either by using single or double quotes:

x = "John"                      # " " is the same as ' '
x = 'John'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)                        # ans = Orange
print(y)                        # ans = Banana
print(z)                        # ans = Cherry

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# You can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)                        # ans = Orange
print(y)                        # ans = Orange
print(z)                        # ans = Orange

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# OUTPUT VARIABLES

# The Python "PRINT" statement is often used to output variables.
# To combine both text and a variable, Python uses the "+" character:

x = "awesome"
print("Python is " + x)         # ans = Python is awesome

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# You can also use the + character to add a variable to another variable:

x = "Python is "
y = "awesome"
z =  x + y
print(z)                        # ans = Python is awesome

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)                    # ans = 15

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# If you try to combine a string and a number, Python will give you an error:

# x = 5
# y = "John"
# print(x + y)                  # ans = TypeError

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# GLOBAL VARIABLES

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"
def myfunc():
  print("Python is " + x)       # ans = Python is awesome
myfunc()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# From def myfuc(): to myfunc() is one function so we get ans 1
# and PRINT command after myfuc() is another function so we get ans 2
x = "awesume"
def myfunc():
  x = "fantasticc"
  print("Python is " + x)       # ans 1 = Python is fantasticc
myfunc()
print("Python is " + x)         # ans 2 = Python is awesume

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# GLOBAL KEYWORDS

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)         # ans = Python is fantastic

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)         # ans = Python is fantastic

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
