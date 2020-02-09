# PYTHON OPERATORS

# Operators are used to perform operations on variables and values. Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# = = = = = = = = = = = = = = = = = = = =

# PYTHON ARITHMETIC OPERATORS are used with numeric values to perform common mathematical operations:

#   Operator	 Name	              Example	   # explanation
#   +	         Addition	          x + y
#   -	         Subtraction	      x - y
#   *	         Multiplication	      x * y
#   /	         Division	          x / y
#   %	         Modulus	          x % y        # 5 % 2 = 1 ?
#   **	         Exponentiation	      x ** y       # (2 ** 5) same as 2*2*2*2*2 = 32
#   //	         Floor division	      x // y       # 15 // 2 = 7 (the floor division // rounds the result
                                                                  # down to the nearest whole number)

# = = = = = = = = = = = = = = = = = = = =

# PYTHON ASSIGNMENT OPERATORS are used to assign values to variables:

#   Operator	Example	      Same As	        # Explanation
#   =	        x = 5	      x = 5             Equals to
#   +=	        x += 3	      x = x + 3         x = 5 & x += 3 gives 8
#   -=	        x -= 3	      x = x - 3         x = 5 & x -= 3 gives 2
#   *=	        x *= 3	      x = x * 3         x = 5 & x *= 3 gives 15
#   /=	        x /= 3	      x = x / 3         x = 5 & x /= 3 gives 1.6666666666666667
#   %=	        x %= 3	      x = x % 3         x = 5 & x %= 3 gives 2 ???
#   //=	        x //= 3	      x = x // 3        x = 5 & x //= 3 gives 1
#   **=	        x **= 3	      x = x ** 3        x = 5 & x **= 3 gives 125
#   &=	        x &= 3	      x = x & 3         x = 5 & x &= 3 gives 1 ???
#   |=	        x |= 3	      x = x | 3         x = 5 & x |= 3 gives 7 ???
#   ^=	        x ^= 3	      x = x ^ 3         x = 5 & x ^= 3 gives 6 ???
#   >>=	        x >>= 3	      x = x >> 3        x = 5 & x >>= 3 gives 0 ???
#   <<=	        x <<= 3	      x = x << 3        x = 5 & x <<= 3 gives 40 ???

# = = = = = = = = = = = = = = = = = = = =

# PYTHON COMPARISON OPERATORS
# Comparison operators are used to compare two values:

#   Operator  Name	                    Example	    # Variable      # Print     # Output    # Explanation
#   ==	      Equal	                    x == y	    x = 5 & y = 3   x == y      False       5 is not equal to 3
#   !=	      Not equal	                x != y      x = 5 & y = 3   x != y      True        5 is not equal to 3
#   >	      Greater than	            x > y       x = 5 & y = 3   x > y       True        5 is greater than 3
#   <	      Less than	                x < y       x = 5 & y = 3   x < y       False       5 is not less than 3
#   >=	      Greater than or equal to	x >= y      x = 5 & y = 3   x >= y      True        5 is greater, or =, to 3
#   <=	      Less than or equal to	    x <= y      x = 5 & y = 3   x >= y      False       5 is nthr les, or = to 3

# = = = = = = = = = = = = = = = = = = = =

# PYTHON LOGICAL OPERATORS. Logical operators are used to combine conditional statements:

#   Operator	Variable  Print	                Output
#   and      	x = 5     (x > 3 and x < 10)    True [if both statements are true][5 is > then 3 & 5 is < then 10]
#   or	        x = 5     (x > 3 or x < 4)      True [if one of the statements is true][5 is > then 3 & 5 is < then 4]
#   not	        x = 5     (not(x > 3 & x < 10)) False Reverse the result [returns False if the result is true]

# = = = = = = = = = = = = = = = = = = = =

# PYTHON IDENTITY OPERATORS

# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

#   Operator	Description	Example	                                        Example
#   is 	        Returns true if both variables are the same object	        x is y
#   is not  	Returns true if both variables are not the same object	    x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)                 # ans = True [Because z is the same object as x]
print(x is y)                 # ans = False [Because x is not the same object as y, even if they have the same content]
print(x == y)                 # ans = True [to demonstrate the difference betweeen "is" and "==":
                                            # this comparison returns True because x is equal to y]

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)             # ans = False [Because z is the same object as x]
print(x is not y)             # ans = True  [Because x is not the same object as y, even if they have the same content]
print(x != y)                 # ans = False [to demonstrate the difference betweeen "is not" and "!=":
                                             # this comparison returns False because x is equal to y]

# = = = = = = = = = = = = = = = = = = = =

# PYTHON MEMBERSHIP OPERATORS
# Membership operators are used to test if a sequence is presented in an object:

#   Operator	Description	Example	                                                                Example
#   in 	        Returns True if a sequence with the specified value is present in the object	    x in y
#   not in	    Returns True if a sequence with the specified value is not present in the object	x not in y

x = ["apple", "banana"]
print("banana" in x)            # ans = True [because a sequence with the value "banana" is in the list]

x = ["apple", "banana"]
print("pineapple" not in x)     # ans = True [because a sequence with the value "pineapple" is not in the list]

# = = = = = = = = = = = = = = = = = = = =

# PYTHON BITWISE OPERATORS
# Bitwise operators are used to compare (binary) numbers:

#  Operator	  Name	                  Description
#   & 	      AND	                  Sets each bit to 1 if both bits are 1
#   |	      OR	                  Sets each bit to 1 if one of two bits is 1
#   ^	      XOR	                  Sets each bit to 1 if only one of two bits is 1
#   ~ 	      NOT	                  Inverts all the bits
#   <<	      Zero fill left shift	  Shift left by pushing zeros in from the right and let the leftmost bits fall off
#   >>	      Signed right shift	  Shift right by pushing copies of the leftmost bit in from the left,
                                      # and let the rightmost bits fall off

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -