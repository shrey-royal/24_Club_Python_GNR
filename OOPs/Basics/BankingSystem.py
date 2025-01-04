class BankAccount:

    def __init__(self, account_number, account_holder, account_type, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def transfer(self, recipient_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transfer successful! New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance for the transfer.")
        else:
            print("Invalid transfer amount.")

    def display(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}\n")


def main():
    acc1 = BankAccount(101, "Alice", "Savings", 1000)
    acc2 = BankAccount(102, "Bob", "Checking", 2000)

    acc1.display()
    acc2.display()

    acc1.deposit(500)

    acc2.withdraw(300)

    acc1.transfer(acc2, 700)

    acc1.display()
    acc2.display()


if __name__ == "__main__":
    main()