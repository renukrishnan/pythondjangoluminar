#constructor: to intialise instance variables
#constructor: automatically invoke when creating objects

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name:",self.name)
        print("age:",self.age)
obj=Person("anu",23)
obj.printvalue()