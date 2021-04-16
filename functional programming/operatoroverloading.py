class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
print(b1+b2)
#if you have three book type to add
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)

    def __sub__(self, other):
        return Book(self.pages - other.pages)

    def __mul__(self, other):
        return Book(self.pages + other.pages)
    def __truediv__(self, other):
        return Book(self.pages + other.pages)
    def __str__(self):
        return str(self.pages)
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1+b2+b3)
print(b2-b1-b3)