from sys import argv

func = argv[1]
amount = int(argv[2])


class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath):
        Account.__init__(self, filepath)


account = Account("balance.txt")
print(account.balance)

if func == "d":
    account.deposit(amount)
elif func == "w":
    account.withdraw(amount)
else:
    print("Enter d for deposit or w for withdraw")

print(account.balance)

checking = Checking("balance.txt")
checking.deposit(199)

print(checking.balance)
account.commit()
checking.commit()
