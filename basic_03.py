#python object practice

'''
exercise:
1. Define a class named `Car`. The `Car` class should have the following attributes: `brand`, `model`, and `year`.
2. The `Car` class should also have a method named `start_engine` that prints a message saying the car is starting.
3. Create two objects of the `Car` class: `car1` and `car2`.
4. Set the `brand`, `model`, and `year` attributes for both `car1` and `car2`.
5. Call the `start_engine` method for both `car1` and `car2`.
6. Print the `brand`, `model`, and `year` of both `car1` and `car2`.

Once you've completed the task, you can share your code with me and I'll review it for you. Good luck! 😊

'''

'''
class Car():
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year

    def start_engine(self):
        print("Car is starting")

car1 = Car("Toyota", "AK47", "2000")
car2 = Car("Ferrari", "69", "2090")

print(f"Car 1: {car1.brand} {car1.model} {car1.year}")
car1.start_engine()

print(f"Car 2: {car2.brand} {car2.model} {car2.year}")
car2.start_engine()


'''


'''

Sure, here's a more challenging exercise for you:

1. Define a class `BankAccount` with the following attributes: `account_number`, `account_name`, and `balance`. The `balance` is initially `0`.
2. Add the following methods to the `BankAccount` class:
    - `deposit(amount)`: Adds the amount to the balance.
    - `withdraw(amount)`: Subtracts the amount from the balance. If the balance is less than the amount, print a message that says "Insufficient balance."
3. Define a class `BankUser` with the following attributes: `user_name` and `accounts`. `accounts` is a list of `BankAccount` objects.
4. Add the following methods to the `BankUser` class:
    - `add_account(account)`: Adds a `BankAccount` object to the `accounts` list.
    - `remove_account(account_number)`: Removes the `BankAccount` object with the matching `account_number` from the `accounts` list.
    - `get_total_balance()`: Returns the sum of the balances of all `BankAccount` objects in the `accounts` list.
5. Create a `BankUser` object and several `BankAccount` objects. Add the `BankAccount` objects to the `BankUser` object using the `add_account` method. Test the `deposit`, `withdraw`, `remove_account`, and `get_total_balance` methods.

Once you've completed the task, you can share your code with me and I'll review it for you. Good luck! 😊


'''

#lets starts
class BankAccount():
    def __init__(self,account_number,account_name,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance

        if self.balance != 0:
            self.balance=self.balance
        else:
            self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
    def withdraw(deposit):

        if self.balance !=0:
            self.balance=self.balance - self.amount
        else:
            print("Insufficient balance")

    class BankUser(BankAccount):
        def add_account(self,account):
            self.account=account
            account=[]
            account=account+self.account


        def remove_account(self):
            account=account - self.account_number

        def get_total_balance(self):
            print(self.balance)

    BankAccount1=BankAccount(1327,"shafikul",0)
    BankAccount2=BankAccount(1325,"shafikula",0)
    BankAccount3=BankAccount(1321,"shafikuluu",0)

    BankUser.add_account(BankAccount1+BankAccount2+BankAccount3)

    BankAccount1.deposit(1000)
    BankAccount1.withdraw(1000)
    BankUser.remove_account(BankAccount3)
    


    ###
    Great job on attempting the exercise! Here are a few points of feedback:

1. In your `withdraw` method, you've written `deposit` as the parameter instead of `amount`. Also, you need to include `self` as the first parameter in the method definition.

2. The `BankUser` class should not be nested inside the `BankAccount` class. These should be two separate classes.

3. In the `BankUser` class, you should initialize `accounts` as an empty list in the `__init__` method.

4. In the `add_account` method, you're trying to add an account to an empty list that you just created. Instead, you should add the account to the `accounts` attribute of the `BankUser` object.

5. In the `remove_account` method, you're trying to subtract an account number from a list of accounts. Instead, you should remove the account with the matching account number from the list.

6. In the `get_total_balance` method, you're printing the balance of the `BankUser` object, but `BankUser` doesn't have a `balance` attribute. Instead, you should calculate the total balance of all accounts in the `accounts` list.

7. When you're creating your `BankUser` object and adding accounts, you're calling `add_account` on the `BankUser` class instead of an instance of the class. You should create a `BankUser` object and call `add_account` on that object.

Here's how your corrected code might look:

```python
class BankAccount():
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

class BankUser():
    def __init__(self, user_name):
        self.user_name = user_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        self.accounts = [account for account in self.accounts if account.account_number != account_number]

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)

# Create BankAccount objects
account1 = BankAccount(1327, "shafikul")
account2 = BankAccount(1325, "shafikula")
account3 = BankAccount(1321, "shafikuluu")

# Create a BankUser object
user = BankUser("User1")

# Add accounts to the user
user.add_account(account1)
user.add_account(account2)
user.add_account(account3)

# Deposit and withdraw money
account1.deposit(1000)
account1.withdraw(500)

# Remove an account
user.remove_account(1321)

# Print total balance
print(user.get_total_balance())
```

Keep practicing, and you'll get the hang of it! 😊