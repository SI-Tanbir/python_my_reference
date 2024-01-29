#formating your text in python
firstname="alxa sins"
lastname="sons of jonny sins" # :))
print("who is your father %s"%firstname)
print("i am {} {}".format(firstname,lastname))

'''
In Python, packing is a way to combine multiple values into a single variable, while unpacking is the opposite: it allows you to extract values from a variable and assign them to separate variables. Packing is done using the * operator, while unpacking is done using the same operator in front of the variable name.

Here’s an example of packing:

Python
'''
def my_sum(*args):
    return sum(args)

result = my_sum(1, 2, 3, 4, 5)
'''

In this example, the *args parameter packs all the arguments passed to the function into a single tuple. The sum() function then calculates the sum of all the values in the tuple.

Here’s an example of unpacking:

Python
'''
my_list = [1, 2, 3, 4]
a, b, c, d = my_list
'''
In this example, the *my_list operator unpacks the list into separate variables a, b, c, and d.
'''

# #now we will learn file handeling in python

# text=input("Why you like pyhton: ")
# with open("fun.txt","w")as f:
#     f.write(text)

# ask the user why they like Python
text = input("Why do you like Python: ")

# open the file "fun.txt" in write mode
with open("fun.txt", "a") as f:
    # write the user's input to the file
    f.write(text)
