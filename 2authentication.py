admin1='shafikul'
pass1="hello"

first_input=input("Enter your user name: \n")
second_input=input("Enter your password: \n")

if(first_input != admin1 ):
    print("wrong user name")

elif(first_input == admin1 and second_input != pass1):
    print("wrong password")

elif(first_input == admin1 and second_input == pass1):
    print("welcome  %s" % admin1)
    



