#class having same method name and same attributes , then child class method will over ride parent class method .. means child class method will execute.
class Parent:
    def properties(self):
        print("10 lakh rs, 2 car")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")
c=Child()
c.marry()