# class: design pattern


class Person:
    def walk(self):
        print("person is walking")
    def run(self):
        print("person is running")

    def jumping(self):
        print("person is jumping")

obj=Person()# obj is the reference created for the class person

obj.walk()
obj.run()
obj.jumping()

ab=Person()# we can create many objects for the same class... ab is another object
ab.walk()