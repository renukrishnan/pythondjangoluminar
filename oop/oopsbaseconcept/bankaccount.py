#using instant variable
class Bank:
    def acCreate(self,acno,name,bname):
        self.bname=bname
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amt):
        self.balance+=amt
        print("your account has been credited with amount", amt)
        print("your current balance:", self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",amt)
            self.balance-=amt
            print("available balance", self.balance)
obj= Bank()
obj.acCreate(201,"renu","sbi")
obj.deposit(25000)
obj.withdraw(15000)