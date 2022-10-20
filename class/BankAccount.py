class BankAccount:
    def __init__(self):
        self.__balance = 0 
    
    def withdraw(self,amount):
        self.__balance -= amount
        print("통장에 " ,amount ,"가 입금 되었음")
        return self.__balance

    def deposit(self,amount):
        self.__balance +=amount
        print("통장에서 " , amount , "가 출금되었음")


a = BankAccount()
a.deposit(100)
a.withdraw(10)

#Frame : global frame : BankAccount, a
#Object : __init__, deposit, withdraw, _BankAccount__balance 

