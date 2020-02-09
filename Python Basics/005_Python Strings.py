# PYTHON STRINGS

# String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
print('Hello')                                          # ans = Hello

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)                                                 # ans = Hello

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes or single quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)                                                  # ans = Lorem ipsum....

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)                                                  # ans = Lorem ipsum....

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STRINGS ARE ARRAYS

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])                                               # ans = e

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# SLICING

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])                                             # ans = llo
# This will include the character from 2 to 5, but will not include the 5th character that is a comma ,
# As per Python indexing H=0, e=1 and so on...

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Get the characters from position 5 to position 1, starting the count from the end of the string:
b = "Hello, World!"
print(b[-5:-2])                                           # ans = orl

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STRING LENGTH

# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))                                             # ans = 13

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STRING METHODS

# Python has a set of built-in methods that you can use on strings.
# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip())                                          # ans = returns "Hello, World!"

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())                                          # ans = hello, world!

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())                                          # HELLO, WORLD!

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J",))                               # ans = Jello, World!

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']        # ans = ['Hello', ' World!']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHECK STRING

# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)                                                  # ans = True

# Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)                                                  # ans = False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STRING CONCATENATION

# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)                                                  # ans = HelloWorld

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)                                                  # ans = Hello World

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STRING FORMAT

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age
# print(txt)                                              # ans = TypeError:

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))                                    # ans = My name is John, and I am 36

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))             # ans = I want 3 pieces of item 567 for 49.95 dollars.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))              # ans = I want to pay 49.95 dollars for 3 pieces of item 567.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ESCAPE CHARACTER

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

# txt = "We are the so-called "Vikings" from the north."    # ans = TypeError

# To fix this problem, use the escape character \":
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:
# Code              Result

# \'	            Single Quote
txt = 'It\'s alright.'
print(txt)          # ans = It's alright.

# \\	            Backslash
txt = "This will insert one \\ (backslash)."
print(txt)          # ans = This will insert one \ (backslash).

# \n	            New Line
txt = "Hello\nWorld!"
print(txt)          # ans = Hello
                    # World!

# \r	            Carriage Return
txt = "Hello\rWorld!"
print(txt)          # ans = Hello
                    # World!

# \t	            Tab
txt = "Hello\tWorld!"
print(txt)          # Hello   World

# \b	            Backspace
txt = "Hello \bWorld!"        # This example erases one character (backspace):
print(txt)          # HelloWorld!

# \f	            Form Feed
txt = "\110\145\154\154\157"   # A backslash followed by three integers will result in a octal value:
print(txt)          # Hello

# \ooo	            Octal value
txt = "\x48\x65\x6c\x6c\x6f"    # A backslash followed by an 'x' and a hex number represents a hex value:
print(txt)          # Hello

# \xhh	            Hex value
txt = "\x48\x65\x6c\x6c\x6f"    # A backslash followed by an 'x' and a hex number represents a hex value:
print(txt)          # Hello

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# STRING METHODS

# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.

# Method	                                    Description

# capitalize()	                                Converts the first character to upper case
txt = "capitalize"
txt = txt.capitalize()
print(txt)                                      # Output - Capitalize
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# casefold()	                                Converts string into lower case
txt = "CASE FOLD"
txt = txt.casefold()
print(txt)                                      # Output - case fold
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# center()	                                    Returns a centered string
txt = "center"
txt2 = txt.center(24)
print(txt2)                                     # Output -          center
txt2 = txt.center(18, '*')
print(txt2)                                     # Output - ******center******
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# count()	                                    Returns the number of times a specified value occurs in a string
txt = "coount"
txt3 = txt.count('o')
print("o's count is: ", txt3)                   # Output - o's count is:  2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# encode()	                                    Returns an encoded version of the string
txt = "encode"
txt_utf = txt.encode()
print("encoded text is: ", txt_utf)             # Output - encoded text is:  b'encode'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# endswith()	                                Returns true if the string ends with the specified value
txt = "Ends With"
txt = txt.endswith("With")
print("Endswith", txt)                          # Output - True
#txtf = txt.endswith("Hello")
#print("Endswith: ", txtf)                      # Output - True
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# expandtabs()	                                Sets the tab size of the string

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# find()	                                    Searches the string for a specified value and returns the
                                                # position of where it was found
txt = "find"
txt = txt.find('n')
print("n is in index of: ", txt)                # Output - n is in index of:  2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# index()	          Searches the string for a specified value and returns the position of where it was found
# The syntax of index() method for string is: str.index(sub[, start[, end]] )
# index() With Substring argument Only
sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)
# result = sentence.index('Java')
# print("Substring 'Java':", result)

# index() With start and end Arguments
sentence = 'Python programming is fun.'

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
# print(sentence.index('fun', 7, 18))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isalnum()	          Returns True if all characters in the string are alphanumeric
# string.isalnum()
name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())

name = "M0n1caG3ll3r"

if name.isalnum() == True:
   print("All characters of string (name) are alphanumeric.")
else:
    print("All characters are not alphanumeric.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isalpha()	          Returns True if all characters in the string are in the alphabet
# string.isalpha()
name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())

name = "MonicaGeller"

if name.isalpha() == True:
   print("All characters are alphabets")
else:
    print("All characters are not alphabets.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isdecimal()	      Returns True if all characters in the string are decimals
# string.isdecimal()
s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

s = '23455'
print(s.isdecimal())
#s = '²3455'
s = '\u00B23455'
print(s.isdecimal())
# s = '½'
s = '\u00BD'
print(s.isdecimal())
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isdigit()	          Returns True if all characters in the string are digits
# string.isdigit()
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())

s = '23455'
print(s.isdigit())
#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())
# s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isidentifier()	  Returns True if the string is an identifier
# string.isidentifier()
str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())

str = 'root33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = '33root'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = 'root 33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# islower()	          Returns True if all characters in the string are lower case
# string.islower()
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

# Usage in program
s = 'this is good'
if s.islower() == True:
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')

s = 'this is Good'
if s.islower() == True:
    print('Does not contain uppercase letter.')
else:
    print('Contains uppercase letter.')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isnumeric()	      Returns True if all characters in the string are numeric




# isprintable()	      Returns True if all characters in the string are printable
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# isspace()	          Returns True if all characters in the string are whitespaces

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# istitle()	          Returns True if the string follows the rules of a title
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# isupper()	          Returns True if all characters in the string are upper case
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# join()	          Joins the elements of an iterable to the end of the string
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ljust()	          Returns a left justified version of the string
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# lower()	          Converts a string into lower case
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# lstrip()	          Returns a left trim version of the string
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# maketrans()	      Returns a translation table to be used in translations
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# partition()	      Returns a tuple where the string is parted into three parts
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# replace()	          Returns a string where a specified value is replaced with a specified value
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# rfind()	          Searches the string for a specified value and returns the last position of where it was found
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# rindex()	          Searches the string for a specified value and returns the last position of where it was found
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# rjust()	          Returns a right justified version of the string
# rpartition()	      Returns a tuple where the string is parted into three parts
# rsplit()	          Splits the string at the specified separator, and returns a list
# rstrip()	          Returns a right trim version of the string
# split()	          Splits the string at the specified separator, and returns a list
# splitlines()	      Splits the string at line breaks and returns a list
# startswith()	      Returns true if the string starts with the specified value
# strip()	          Returns a trimmed version of the string
# swapcase()	      Swaps cases, lower case becomes upper case and vice versa
# title()	          Converts the first character of each word to upper case
# translate()	      Returns a translated string
# upper()	          Converts a string into upper case
# zfill()	          Fills the string with a specified number of 0 values at the beginning

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''
# format()	          Formats specified values in a string
# .format has thee arguments ... 1. Default, 2. Positional, 3. Keyword and 4. Mixed
print("Default Argument - Hello {}, your balance is {}.".format("Adam", 230.2346))
print("Positional Argument - Hello {0}, your balance is {1}.".format("Adam", 230.2346))
print("Keyword Argument - Hello {name}, your balance is {bal}.".format(name="Adam", bal=230.2346))
print("Mixed Argument - Hello {0}, your balance is {bal}.".format("Adam", bal=230.2346))

# Numbers formatting with format()
# You can format numbers using the format specifier given below:
# Number Formatting Types
# Type	Meaning
# d	    Decimal integer
# c	    Corresponding Unicode character
# b	    Binary format
# o	    Octal format
# x	    Hexadecimal format (lower case)
# X	    Hexadecimal format (upper case)
# n	    Same as 'd'. Except it uses current locale setting for number separator
# e	    Exponential notation. (lowercase e)
# E	    Exponential notation (uppercase E)
# f	    Displays fixed point number (Default: 6)
# F	    Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
# g	    General format. Rounds number to p significant digits. (Default precision: 6)
# G	    Same as 'g'. Except switches to 'E' if the number is large.
# %	    Percentage. Multiples by 100 and puts % at the end.

print("The interger argument is: {:d}".format(123))
print("The float argument is: {:f}".format(123.4567898))
print("binary: {0:b}, octal: {0:o}, hexadecimal: {0:X}".format(12))
print("n Same as 'd'. Except it uses current locale setting for number separator - argument is: {:n}".format(123))
print("e Exponential notation argument is: {:E}".format(123))
print("f Displays fixed point number (Default: 6): {:f}".format(123))
print("g General format. Rounds number to p significant digits. (Default precision: 6): {:g}".format(123.4567898))
print("% Percentage. Multiples by 100 and puts % at the end.: {:%}".format(123))

# *** Number formatting with padding for int and floats ***

# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

# *** Number formatting for signed numbers ***
# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

# *** Number formatting with alignment ***

# Type	Meaning
# <	    Left aligned to the remaining space
# ^	    Center aligned to the remaining space
# >	    Right aligned to the remaining space
# =	    Forces the signed (+) (-) to the leftmost position

# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))

# *** String formatting with padding and alignment ***

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))

# *** Truncating strings with format() ***

# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters, padding and center alignment
print("{:^5.3}".format("caterpillar"))

# *** Formatting class members using format() ***

# define Person class
class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))

# *** Formatting dictionary members using format() ***

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))

# There's an easier way to format dictionaries in Python using str.format(**mapping).
# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))

# ** is a format parameter (minimum field width).

# *** Dynamic formatting using format() ***

# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))

# *** Type-specific formatting with format() and overriding __format__() method ***

import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adam's age is: {:age}".format(Person()))

# *** __str()__ and __repr()__ shorthand !r and !s using format() ***

# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))

# __str__() and __repr__() implementation for class
class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p=Person()))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# format_map()          Formats specified values in a string

# str.format(**mapping)
point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))

# *** How format_map() works? ***
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

# *** How format_map() works with dict subclass? ***
class Coordinate(dict):
    def __missing__(self, key):
      return key

print('({x}, {y})'.format_map(Coordinate(x='6')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))

'''


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
