class BankAccount:
    def __init__(self, bankname=" ", ownername=" ", accountnumber=" ", currentbalance=0) -> None:
        self.bankname = bankname
        self.ownername = ownername
        self.accountnumber = accountnumber
        self.currentbalance = currentbalance

    def print_out(self):
        print(f"Bank name: {self.bankname} \nOwner name: {self.ownername} \nAccount number: {self.accountnumber} \nCurrent balance: {self.currentbalance}")

    def deposit(self, d=0):
        if 0 <= d :
            self.currentbalance += d
        else:
            self.currentbalance
        print(f"Current balance: {self.currentbalance}")

    def withdraw(self, w=0):
        if 0 <= w <= self.currentbalance:
            self.currentbalance -= w
        else:
            self.currentbalance
        print(f"Current balance: {self.currentbalance}")


bank = BankAccount("SCB", "Bowornthat Chainngthong", "12-12145189", 2000)
bank.print_out()
bank.deposit(1100)
bank.withdraw(4000)
bank.withdraw(200)
