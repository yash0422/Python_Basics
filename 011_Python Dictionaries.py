# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# PYTHON DICTIONARIES

# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with {  curly brackets  }, and they have keys and values.
# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)                                   # ans = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ACCESSING ITEMS

# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)                                          # ans = Mustang

# There is also a method called <<  get()  >> that will give you the same result:
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)                                          # ans = Mustang

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHANGE VALUES

# You can change the value of a specific item by referring to its key name:
# Change the "year" to 2018:
thisdict = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
 }
thisdict["year"] = 2018
print(thisdict)                                   # ans = {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# LOOP THROUGH A DICTIONARY

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
# Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
   print(x)                                       # ans = brand -- model -- year


# Print all values in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
   print(thisdict[x])                             # ans = Ford -- Mustang -- 1964

# You can also use the <<  values()  >> function to return values of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)                                        # ans = = Ford -- Mustang -- 1964

# Loop through both keys and values, by using the <<  items()  >> function:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)                                     # ans = brand Ford  --  model Mustang  --  year 1964

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# CHECK IF KEY EXISTS

# To determine if a specified key is present in a dictionary use the in keyword:
# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  # ans = Yes, 'model' is one of the keys in the thisdict dictionary

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DICTIONARY LENGTH

# To determine how many items (key-value pairs) a dictionary has, use the <<  len()  >> method.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))                              # ans = 3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# ADDING ITEMS

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)                                   # ans = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# REMOVING ITEMS

# There are several methods to remove items from a dictionary:
# The <<  pop()  >> method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)                                    # ans = {'brand': 'Ford', 'year': 1964}

# The <<  popitem()  >> method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)                                   # ans = {'brand': 'Ford', 'model': 'Mustang'}

# The <<  del  >> keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)                                   # ans = {'brand': 'Ford', 'year': 1964}

# The <<  del  >> keyword can also delete the dictionary completely:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thislist" no longer exists.

# The <<  clear()  >> keyword empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)                                    # ans = {}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# COPY A DICTIONARY

# You cannot copy a dictionary simply by typing <<  dict2 = dict1  >>, because: <<  dict2  >> will only be a reference
# to <<  dict1  >>, and changes made in <<  dict1  >> will automatically also be made in <<  dict2  >>.
# There are ways to make a copy, one way is to use the built-in Dictionary method <<  copy()  >>.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)                                       # ans = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Another way to make a copy is to use the built-in method <<  dict()  >>.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)                                       # ans = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# NESTED DICTIONARIES

# A dictionary can also contain many dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
# ans = {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007},
# 'child3': {'name': 'Linus', 'year': 2011}}

# Or, if you want to nest three dictionaries that already exists as dictionaries:
# Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
# ans = {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007},
# 'child3': {'name': 'Linus', 'year': 2011}}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# THE <<  dict()  >> CONSTRUCTOR

# It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)                                   # ans = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DICTIONARY METHODS

# Python has a set of built-in methods that you can use on dictionaries.

#   Method	          Description

#   clear()	          Removes all the elements from the dictionary
#   copy()	          Returns a copy of the dictionary
#   fromkeys()	      Returns a dictionary with the specified keys and values
#   get()	          Returns the value of the specified key
#   items()	          Returns a list containing a tuple for each key value pair
#   keys()	          Returns a list containing the dictionary's keys
#   pop()	          Removes the element with the specified key
#   popitem()	      Removes the last inserted key-value pair
#   setdefault()	  Returns the value of the specified key. If the key does not exist: insert the key,
#                     with the specified value
#   update()	      Updates the dictionary with the specified key-value pairs
#   values()	      Returns a list of all the values in the dictionary

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# DICTIONARY EXPLANATION FROM EDUREKA