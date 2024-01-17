a,b = 3,4
print(a,b)

#exercise

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)



#additional

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = ["khan","magibaj","rhoman"]
strings.append("hello")
strings.append("world")
numbers.append(1)
numbers.append(2)
numbers.append(3)
# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name[1])


even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


remainder = 11 % 3
print(remainder)