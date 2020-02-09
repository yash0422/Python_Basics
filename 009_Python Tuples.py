# TUPLE

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)                                # ans = ('apple', 'banana', 'cherry')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ACCESS TUPLE ITEMS

# You can access tuple items by referring to the index number, inside square brackets:
# Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])                             # ans = banana

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# NEGATIVE INDEXING

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])                            # ans = cherry

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# RANGE OF INDEXES

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])                           # ans = ('cherry', 'orange', 'kiwi')

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# RANGE OF NEGATIVE INDEXES

# Specify negative indexes if you want to start the search from the end of the tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])                         # ans = ('orange', 'kiwi', 'melon')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHANGE TUPLE VALUES

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)                                         # ('apple', 'kiwi', 'cherry')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LOOP THROUGH A TUPLE

# You can loop through the tuple items by using a for loop.
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)                                        # ans = cherry

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHECK IF ITEM EXISTS

# To determine if a specified item is present in a tuple use the in keyword:
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")    # ans = Yes, 'apple' is in the fruits tuple

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# TUPLE LENGTH

# To determine how many items a tuple has, use the len() method:
# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))                             # ans = 3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ADD ITEMS

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# You cannot add items to a tuple:
# thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange" # This will raise an error
# print(thistuple)                                # ans = error

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CREATE TUPLE WITH ONE ITEM

# To create a tuple with only one item, you have add a comma after the item,
# unless Python will not recognize the variable as a tuple.

# One item tuple, remember the commma:

thistuple = ("apple",)
print(type(thistuple))                            # ans = <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))                            # ans = <class 'str'>

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# REMOVE ITEMS

# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
# The del keyword can delete the tuple completely:

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)                                # ans = error as list does not exists

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# JOIN TWO TUPLES

# To join two or more tuples you can use the + operator:
# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)                                       # ans = ('a', 'b', 'c', 1, 2, 3)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# THE <<  tuple()  >> CONSTRUCTOR

# It is also possible to use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry"))    # note the double round-brackets
print(thistuple)                                    # ans = ('apple', 'banana', 'cherry')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# TUPLE METHODS

# Python has two built-in methods that you can use on tuples.

#   Method	      Description
#   count()	      Returns the number of times a specified value occurs in a tuple
#   index() 	  Searches the tuple for a specified value and returns the position of where it was found

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -