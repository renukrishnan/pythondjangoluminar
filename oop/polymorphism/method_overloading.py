#python not supoorting method overloading
#when super class and derived class having same method(here it is show(), but the no. of attributes is different . that is overloading
class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)
per=Student()
per.show(3,4)# here it will execute derived class show() method coz of two attributes
per.show(5)#it won"t work here coz overloading concept is not supporting in python