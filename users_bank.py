class BankAccount:
    def __init__(self, int_rate =0.05, balance = 100): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else: 
            print(f"You don't have enough cash to make a withdrawl, there will be a $5 fee added to your account.")
        return self

    def display_account_info(self):
        print(self.balance)
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print ("Sorry, not enough cash")
        return self

kye_account = BankAccount()
quinn_account = BankAccount()

kye_account.display_account_info()
quinn_account.display_account_info()

kye_account.deposit(10).deposit(90).deposit(45).withdraw(30).yield_interest().display_account_info()
quinn_account.deposit(40).deposit(20).deposit(30).withdraw(10).yield_interest().display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "spending" : BankAccount(.05,100),
            "savings" : BankAccount(.05,160)
        }

    def user_ammount(self): 
        print(f"User: {self.name}, spending: ${self.account['spending'].display_account_info()}")
        print(f"User: {self.name}, savings: ${self.account['savings'].display_account_info()}")
        return self


    def account_value(self,amount,user):
        self.amount = self.amount - amount
        user.amount = user.amount + amount
        self.user_ammount()
        user.user_ammount()
        return self

Kye = User("Kye")

Kye.account['spending'].withdraw(750)
Kye.account['savings'].deposit(200)
Kye.user_ammount()

