'''

type of method
1. instance method
2. class method
3. static method


'''

class Employee:
    comp="Techsrijan"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def add(self):
        return(self.m1+self.m2+self.m3)

    @classmethod
    def comanyname(cls):
        print(cls.comp)

    @staticmethod
    def ag():
        print("hello")

e1=Employee(10,11,12)
print("Salay=",e1.add())
Employee.comanyname()
e1.comanyname()

Employee.ag()