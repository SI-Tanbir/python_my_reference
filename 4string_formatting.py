

name="shafikul"
age=35

print("hello, %s!\n your age %d" % (name,age))


# Here are some basic argument specifiers you should know:
    
# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)


astring = "Hello world!"
print(astring[3:3])# count start with 0
# print(astring[3:7:1]) how it work i don't know
#print backword
print(astring[::-1])
# upper case word
print(astring.upper())

print(astring.split())


# i have problem  with concept and
# slicing of stirngs  

# Define a sample string
my_string = "Python is awesome!"

# Basic slicing syntax: string[start:stop]

# Example 1: Slice from index 0 to 5 (excluding 5)
substring = my_string[0:5]
print(substring)  # Output: "Pytho"

# Example 2: Slice from index 7 to 9 (excluding 9)
substring = my_string[7:9]
print(substring)  # Output: "is"

# Example 3: Slice from index 10 to the end of the string
substring = my_string[10:]
print(substring)  # Output: "awesome!"

# Example 4: Slice from the beginning to index 6 (excluding 6)
substring = my_string[:6]
print(substring)  # Output: "Python"

# Negative indexing: Counting from the end of the string
# Example 5: Slice from the last character to the end
substring = my_string[-1:]
print(substring)  # Output: "!"

# Example 6: Slice from the second-to-last character to the end
substring = my_string[-2:]
print(substring)  # Output: "e!"

# Step value: string[start:stop:step]
# Example 7: Slice with a step of 2 (every second character)
# my_string = "Python is awesome!"
mystring="0123456789"  #
print(mystring[0::3])  # now i got it it just slice this middle indexing value 

# Example 8: Reverse the string using slicing
substring = my_string[::-1]
print(substring) # Output: "!emosewa si nohtyP"
