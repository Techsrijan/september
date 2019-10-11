class Student:
    def msg(self):
        print("hi")
    def StDetail(self,name,age):
        self.name=name
        self.age=age
        print(name,age)
    def __init__(self):
        print("I will run")

ob=Student()
ob.msg()
ob.StDetail("abc",44)
#Student.msg(ob)
ob1=Student()

