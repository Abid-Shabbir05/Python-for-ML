class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

   
    def get_balance(self,):
        return self.__balance
    
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposite amount is :{self.__balance}"
        else:
            return "amount must be positive"
    
    def withdrow(self, amount ):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdraw amount {amount} new balance = {self.__balance}"
        else:
            return "Invalide withdrawal amount"
        
    
acc = Bankaccount("Abid", 1000)
print(acc.get_balance())
print(acc.deposite(500))
print(acc.withdrow(200))

