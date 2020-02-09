# PYTHON LISTS

# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered and unindexed. No duplicate members.
    # Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning,
# and it could mean an increase in efficiency or security.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LIST

# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)                               # ans = ['apple', 'banana', 'cherry']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ACCESS ITEMS

# You access the list items by referring to the index number:
# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])                            # ans = banana

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# NEGATIVE INDEXING

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])                           # ans = cherry

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# RANGE OF INDEXES

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])                          # ans = ['cherry', 'orange', 'kiwi']

# This will return the items from position 2 to 5.
# Remember that the first item is position 0, and note that the item in position 5 is NOT included
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to "orange":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])                             # ans = ['apple', 'banana', 'cherry', 'orange']

# This will return the items from index 0 to index 4.
# Remember that index 0 is the first item, and index 4 is the fifth item
# Remember that the item in index 4 is NOT included

# By leaving out the end value, the range will go on to the end of the list:
# This example returns the items from "cherry" and to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])                             # ans = ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# RANGE OF NEGATIVE INDEXES

# Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from index -4 (included) to index -1 (excluded)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])                          # ans = ['orange', 'kiwi', 'melon']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHANGE ITEM VALUE

# To change the value of a specific item, refer to the index number:
# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)                                 # ans = ['apple', 'blackcurrant', 'cherry']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LOOP THROUGH A LIST

# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)                                      # ans = cherry

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHECK IF ITEM EXISTS

# To determine if a specified item is present in a list use the in keyword:
# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
   print("Yes, 'apple' is in the fruits list")    # ans = Yes, 'apple' is in the fruits list

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LIST LENGTH

# To determine how many items a list has, use the len() function:
# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))                            # ans = 3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ADD ITEMS

# To add an item to the end of the list, use the append() method:
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)                                 # ans = ['apple', 'banana', 'cherry', 'orange']

# To add an item at the specified index, use the insert() method:
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)                                 # ans = ['apple', 'orange', 'banana', 'cherry']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# REMOVE ITEM

# There are several methods to remove items from a list:
# << .remove()  >> method removes the specified item:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)                                 # ans = ['apple', 'cherry']

# <<  .pop()  >> method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)                                 # ans = ['apple', 'banana']

# <<  del  >> keyword removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)                                 # ans = ['banana', 'cherry']

# <<  del  >> keyword can also delete the list completely:

thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)                               # ans = #this will cause an error because you have succsesfully deleted
                                                #  "thislist". NameError: name 'thislist' is not defined

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# COPY A LIST

# << .copy >>
# You cannot copy a list simply by typing << list2 = list1 >>, because: << list2 >> will only be a reference
# to << list1 >>. And changes made in << list1 >> will automatically also be made in << list2 >>.
# There are ways to make a copy, one way is to use the built-in List method copy().
# Make a copy of a list with the << copy() >> method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)                                   # ans = ['apple', 'banana', 'cherry']

# <<  list()  >>
# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)                                   # # ans = ['apple', 'banana', 'cherry']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# JOIN TWO LISTS

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)                                    # ans = ['a', 'b', 'c', 1, 2, 3]

# Another way to join two lists are by appending all the items from list2 into list1, one by one:
# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)                                    # ['a', 'b', 'c', 1, 2, 3]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# The << list()  >> Constructor. It is also possible to use the list() constructor to make a new list.

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)                                 # ans = ['apple', 'banana', 'cherry']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LIST METHODS

# Python has a set of built-in methods that you can use on lists.
#   Method	        Description

#   append()	    Adds an element at the end of the list
#   clear()	        Removes all the elements from the list
#   copy()  	    Returns a copy of the list
#   count()	        Returns the number of elements with the specified value
#   extend()	    Add the elements of a list (or any iterable), to the end of the current list
#   index()	        Returns the index of the first element with the specified value
#   insert()	    Adds an element at the specified position
#   pop()	        Removes the element at the specified position
#   remove()	    Removes the item with the specified value
#   reverse()	    Reverses the order of the list
#   sort()	        Sorts the list
