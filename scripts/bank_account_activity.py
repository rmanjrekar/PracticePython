class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Customer(Person):
    def __init__(self, firstname, lastname, account_number, balance=0):
        super().__init__(firstname,lastname)
        self.account_number = self._validate_account_number(account_number)
        self.balance = balance
    
    def _validate_account_number(self, account_number):
        if not account_number.isdigit():
            raise ValueError("Account number should only contain digits.")

    def __str__(self):
        return f'Client Details here: {self.firstname} {self.lastname} => Account Balance {self.account_number}: ${self.balance}'

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit accepted")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print('Withdrawal done')
        else:
            print("Low Balance : ", self.balance)


def start():
    cust_obj = create_client()
    user_input = ""
    while user_input != 'E':
        print(cust_obj)
        print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
        user_input = input("Select the category from above : ")
        if user_input == "D" :
            amount = input("Enter the amount : ")
            cust_obj.deposit(int(amount))
        elif user_input == "W" :
            amount = input("Enter the amount : ")
            cust_obj.withdraw(int(amount))
        
    print(f"Thank you {cust_obj.firstname} {cust_obj.lastname} for using this service!")


def create_client():
    firstname = input("Please enter your First Name : ")
    lastname = input("Please enter your Last Name : ")
    account_number = input("Please enter your Account Number : ")
    cust_obj = Customer(firstname, lastname, account_number)
    return cust_obj

start()