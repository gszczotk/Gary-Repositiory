from bank_account import BankAccount

account1 = BankAccount(1234567)
account2 = BankAccount(7654321, 100.00)
account3 = BankAccount(3232323, 7542.50)

print(account1)
print(account2)
print(account3)
print()

account1.deposit(50.00)
account2.withdraw(25.50)
account3.deposit(500.20)
account3.withdraw(700.00)

print(account1)
print(account2)
print(account3)