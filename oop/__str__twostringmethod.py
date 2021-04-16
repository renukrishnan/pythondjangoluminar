class College:
    collegename="Mangalam"

    def __init__(self,name,roll):
        self.roll=roll
        self.name=name
    def printDetails(self):
        print("college name=",self.collegename)
        print("name of student:",self.name)
        print("roll no",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
ob=College("anu",4)
print(ob)
