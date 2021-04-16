class Add():
    def setVal(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printvalue(self):
        self.res=self.num1+self.num2
        print("sum=",self.res)

obj=Add()
obj.setVal(3,5)
obj.printvalue()