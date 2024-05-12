class Account:
    def __init__(self, balace = 0):
        self.balances = balace

    def withdraw(self, amt):
        if self.balances > amt:
            self.balances -= amt
            print(f"{amt} withdrawn successfully ")
        else:
            print("Not enough balance")

    def desposit(self, amt):
        self.balances += amt
        print(f"{amt} successfully deposited ")
    
    def balance(self):
        print(f"Your bank balance is: {self.balances}")


amt = int(input("Enter the opening balance: "))
acc = Account(amt)

while True:
    print("\n------------------- Bank Account ---------------\n")
    print("Operations\n1.Withdraw\n2.Deposit\n3.Balance\n4.Exit")
    ch = int(input("Enter option : "))

    if ch == 1:
        acc.withdraw(int(input("Enter amount to withdraw: ")))
    elif ch == 2:
        acc.desposit(int(input("Enter amount to deposit: ")))
    elif ch == 3:
        acc.balance()
    else:
        break