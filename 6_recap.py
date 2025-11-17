# Learn Python
# Python is a popular programming language.
#
# Python can be used on a server to create web applications.


print("This is our favorite number 123") # Output: This is our favorite number 123



print("Hello World!", end=" ")
print("I will print on the same line.")

# Hello World! I will print on the same line.
# end=" " ata dine same line a code run hobe.
# Note that we add a space after end=" " for better readability.

# Python Variables


# same value to multiple variables in one line:
# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)




fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)




# In the print() function, you output multiple variables, separated by a comma:
# Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# You can also use the + operator to output multiple variables:
# Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".


# Python Numbers
# There are three numeric types in Python:
# int
# float
# complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#
# Example
# Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))






# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#
# Example
# Floats:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))





# Float can also be scientific numbers with an "e" to indicate the power of 10.
#
# Example
# Floats:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


# Complex
# Complex numbers are written with a "j" as the imaginary part:
#
# Example
# Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
#
# Example
# Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Note: You cannot convert complex numbers into another number type.




#string
# multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = "Hello, World!"
print(a[1]) # e

a = "Hello, World!"
print(len(a)) #13


b = "Hello, World!"
print(b[2:5]) # llo


#Note: The first character has index 0.


b = "Hello, World!"
print(b[-5:-2]) #orl


a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!




a = "Hello, World!"
print(a.lower()) # hello, world!


a = " Hello, World! "
print(a.strip()) # Hello, World!


a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!



a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld



a = "Hello"
b = "World"
c = a + " " + b
print(c) # Hello World




age = 36
txt = f"My name is John, I am {age}"
print(txt) # My name is John, I am 36




price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  #The price is 59.00 dollars



txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars


txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # We are the so-called "Vikings" from the north.

#
#
# Escape Characters
# Other escape characters used in Python:
#
# Code	Result	Try it
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value






# Boolean Values
# In programming you often need to know if an expression is True or False.
#
# You can evaluate any expression in Python, and get one of two answers, True or False.
#
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
#
# ExampleGet your own Python Server
print(10 > 9)
print(10 == 9)
print(10 < 9)
# True
# False
# False






# Python Operators
# Operators are used to perform operations on variables and values.
#
# In the example below, we use the + operator to add together two values:
#
# ExampleGet your own Python Server
print(10 + 5) #15




# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
#
# Operator	Name	Example	Try it
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y


# Examples
# Here is an example using different arithmetic operators:
#
# ExampleGet your own Python Server
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)



# 19
# 11
# 60
# 3.75
# 3
# 50625
# 3




# Division in Python
# Python has two division operators:
#
# / - Division (returns a float)
# // - Floor division (returns an integer)
# Example
# Division always returns a float:

x = 12
y = 5

print(x / y) #2.4
# Example
# Floor division always returns an integer.
#
# It rounds DOWN to the nearest integer:

x = 12
y = 5

print(x // y) #2



#
#
# Assignment Operators
# Assignment operators are used to assign values to variables:
#
# Operator	Example	Same As	Try it
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3
# :=	print(x := 3)	x = 3
# print(x)







#
# Comparison Operators
# Comparison operators are used to compare two values:
#
# Operator	Name	Example	Try it
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y
# Examples
# Comparison operators return True or False based on the comparison:
#
# ExampleGet your own Python Server
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


#
# False
# True
# True
# False
# True
# False



#
# Python Logical Operators
# Logical Operators
# Logical operators are used to combine conditional statements:
#
# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
# Examples
# ExampleGet your own Python Server
# Test if a number is greater than 0 and less than 10:

x = 5

print(x > 0 and x < 10) # True



#
#
# Python Identity Operators
# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#
# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y
# Examples
# ExampleGet your own Python Server
# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# True
# False
# True




# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
#
# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
# Examples
# ExampleGet your own Python Server
# Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) #True









#
# Python Bitwise Operators
# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
#
# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
# ~	NOT	Inverts all the bits	~x
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
# Examples
# Example
# ExampleGet your own Python Server
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(6 & 3) #2
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011

# Then the & operator compares the bits and returns 0010, which is 2 in decimal.
#
# Example
# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(6 | 3) #7
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011

# Then the | operator compares the bits and returns 0111, which is 7 in decimal.
#
# Example
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(6 ^ 3)  #5
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
#
# Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.


# Operator Precedence
# Operator precedence describes the order in which operations are performed.
#
# ExampleGet your own Python Server
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3)) #0
# Example
# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

print(100 + 5 * 3) #115
# Precedence Order
# The precedence order is described in the table below, starting with the highest precedence at the top:
#
# Operator	Description	Try it
# ()	Parentheses
# **	Exponentiation
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# not	Logical NOT
# and	AND
# or	OR
# Left-to-Right Evaluation
# If two operators have the same precedence, the expression is evaluated from left to right.
#
# Example
# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3) #5



# Next Python List
