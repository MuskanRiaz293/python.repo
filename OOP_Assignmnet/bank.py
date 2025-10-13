from abc import ABC, abstractmethod
import csv

# Abstract Base Class: Account
class Account(ABC):
    def __init__(self, owner, account_no, balance):
        self.owner = owner
        self.account_no = account_no
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)
        return f"Deposited Rs. {amount}. New balance: Rs. {self.balance}"

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def monthly_process(self):
        pass

# Saving Account
class SavingAccount(Account):
    def __init__(self, owner, account_no, balance, interest_rate):
        super().__init__(owner, account_no, balance)
        self.interest_rate = float(interest_rate)

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -= amount
        return f"Withdrawn Rs. {amount}. Remaining balance: Rs. {self.balance}"

    def monthly_process(self):
        interest = (self.balance * self.interest_rate) / 100 / 12
        self.balance += interest

# Current Account
class CurrentAccount(Account):
    def __init__(self, owner, account_no, balance, loan_limit, fees):
        super().__init__(owner, account_no, balance)
        self.loan_limit = float(loan_limit)
        self.fees = float(fees)

    def withdraw(self, amount):
        if self.balance - amount < -self.loan_limit:
            return "Loan limit exceeded!"
        self.balance -= amount
        return f"Withdrawn Rs. {amount}. New balance: Rs. {self.balance}"

    def monthly_process(self):
        if self.balance < 0:
            self.balance -= self.fees


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add(self, account: Account):
        self.accounts[account.account_no] = account

    def get(self, account_no):
        return self.accounts.get(account_no)

    def transfer(self, from_acc_no, to_acc_no, amount):
        sender = self.get(from_acc_no)
        receiver = self.get(to_acc_no)

        if not sender or not receiver:
            return "Account not found!"
        message = sender.withdraw(amount)
        if "Insufficient" not in str(message) and "exceeded" not in str(message):
            receiver.deposit(amount)
        return f"Transferred Rs.{amount} from {from_acc_no} to {to_acc_no}"

    def show(self):
        print(f"\n {self.name} Accounts:")
        for acc in self.accounts.values():
            print(f"{acc.account_no} | {acc.owner} | Balance: Rs.{acc.balance}")

    def load_from_csv(self, file="accounts.csv"):
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                acc_type = row["Account_type"]
                owner = row["owner"]
                acc_no = row["account_no"]
                balance = float(row["balance"] or 0)

                if acc_type.lower() == "saving":
                    account = SavingAccount(owner, acc_no, balance, float(row["interest_rate"] or 0))
                elif acc_type.lower() == "current":
                    account = CurrentAccount(owner, acc_no, balance, float(row["loan_limit"] or 0), float(row["fees"] or 0))
                else:
                    continue

                self.add(account)
        print("Accounts loaded successfully!")

    def save_to_csv(self, file="accounts_updated.csv"):
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Account_type", "owner", "account_no", "balance", "interest_rate", "loan_limit", "fees"])
            for acc in self.accounts.values():
                if isinstance(acc, SavingAccount):
                    writer.writerow(["Saving", acc.owner, acc.account_no, acc.balance, acc.interest_rate, "", ""])
                elif isinstance(acc, CurrentAccount):
                    writer.writerow(["Current", acc.owner, acc.account_no, acc.balance, "", acc.loan_limit, acc.fees])
        print("Data saved to CSV successfully!")

bank = Bank("Standard Chartered Bank")
bank.load_from_csv("accounts.csv")

bank.show()
bank.get("S-123").deposit(500) 
bank.get("F-321").withdraw(100) 
bank.transfer("S-123", "F-321", 200)
bank.show()
# Save updated data
bank.save_to_csv("accounts_updated.csv")
