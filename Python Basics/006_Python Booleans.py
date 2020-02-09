# PYTHON BOOLEANS

# Boolean Values
# Booleans represent one of two values: True or False. In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)                         # ans = True
print(10 == 9)                        # ans = False
print(10 < 9)                         # ans = False

# Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")        # not executed
else:
  print("b is not greater than a")    # ans = b is not greater than a

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Evaluate a string and a number:
print(bool("Hello"))                  # ans = True
print(bool(15))                       # ans = True

# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))                        # ans = True
print(bool(y))                        # ans = True

# Most Values are True

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings. Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

print(bool("abc"))                                # ans = True
print(bool(123))                                  # ans = True
print(bool(["apple", "cherry", "banana"]))        # ans = True

# Some Values are False
# In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "",
# the number 0, and the value None. And of course the value False evaluates to False.
# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print(bool(False))                                # ans = False
print(bool(None))                                 # ans = False
print(bool(0))                                    # ans = False
print(bool(""))                                   # ans = False
print(bool(()))                                   # ans = False
print(bool([]))                                   # ans = False
print(bool({}))                                   # ans = False

# One more value, or object in this case, evaluates to False, and that is if you have an objects that are made
# from a class with a __len__ function that returns 0 or False:
class myclass():
   def __len__(self):
     return 0

myobj = myclass()
print(bool(myobj))                                # ans = False

# Functions can Return a Boolean
# Python also has many built-in functions that returns a boolean value, like the isinstance() function, which
# can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))                         # ans = True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -