

print("hello world") #my first code run

x = "John"
# is the same as
x = 'John'
print(x)




'''
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
'''
"""
python keywords give blew:--
------------------------------------------------
and	 ---  A logical operator
as	---To create an alias
assert ---For debugging
break ---	To break out of a loop
class---	To define a class
continue	---To continue to the next iteration of a loop
def ---	To define a function
del	 ----To delete an object
elif----	Used in conditional statements, same as else if
else---	Used in conditional statements
except---	Used with exceptions, what to do when an exception occurs
False	---Boolean value, result of comparison operations
finally	---Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	--To create a for loop
from	---To import specific parts of a module
global	---To declare a global variable
if	---To make a conditional statement
import----	To import a module
in	---To check if a value is present in a list, tuple, etc.
is	--To test if two variables are equal
lambda---	To create an anonymous function
None	---Represents a null value
nonlocal	---To declare a non-local variable
not ---	A logical o\erator
or	---A logical operator
pass	---A null statement, a statement that will do nothing
raise	---To raise an exception
return	----To exit a function and return a value
True	----Boolean value, result of comparison operations
try	-----To make  a try...except statement
while	----To create a while loop
with	---Used to simplify exception handling
yield----	To return a list of values from a generator

"""
# assining multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#global variables:--
x="awesome ,global variables"

def myfunciton():
    print("python is "+x)

myfunciton()


'''
The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword

'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
