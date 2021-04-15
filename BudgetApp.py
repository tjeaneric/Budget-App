class Budget:

    def __init__(self, name):

        self.name = name
        self.balance = list()

    def deposit(self, amount, description=""):

        self.balance.append({"amount": amount, "description": description})
        print(f"{amount} deposited successfully to {self.name}")

    def withdraw(self, amount, description=""):

        if(self.checkFunds(amount)):
            self.balance.append(
                {"amount": -amount, "description": description})
            print(f"{amount} withdrawn successfully from {self.name}")    
            return True
            
        return False

    def get_balance(self):
        
        total_cash = 0
        for i in self.balance:
            total_cash += i["amount"]    
        return total_cash

    def check_balance(self):
        total_cash = 0
        for i in self.balance:
            total_cash += i["amount"]    
        return (f"the balance of {self.name}: {total_cash} ")

    def transfer(self, amount, category):
        if(self.checkFunds(amount)):
            self.withdraw(amount, "transfer to" + category.name)
            category.deposit(amount, "transfer from" + self.name)
            print(f"{amount} transferred successfully from {self.name} to {category.name}")
            return True
        print("Transfer failed, Insufficient funds")

    def checkFunds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")
food.deposit(1000)
food.withdraw(300)
food.transfer(200, clothing)
clothing.transfer(190, entertainment)
entertainment.deposit(500)
entertainment.transfer(320, food)
print(food.check_balance())
print(clothing.check_balance())
print(entertainment.check_balance())
