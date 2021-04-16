#single inheritance
class Parent:
    parent_name='arun'
    def m1(self,age):
        self.age=age
        print("my name is", Parent.parent_name)
        print("my age:",self.age)

class Child(Parent):
    def m2(self,cage):
        self.cage=cage
        print("parent name is",Parent.parent_name)
        print("parent age is:",self.age)
        print("child age is:",self.cage)

c=Child()
c.m1(23)
c.m2(2)

