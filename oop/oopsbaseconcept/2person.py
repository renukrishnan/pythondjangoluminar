class Person:
    def setVal(self,name,age):
        self.age=age #self.age means it will accept age as class attribute
        self.name=name

    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)

obj=Person()
obj.setVal("ram",23)
obj.printvalue()