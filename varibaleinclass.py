'''
variable
    1. class variable
    2. instance variable


'''

class Car:
    wheel=4
    def __init__(self):
        self.mil=10
        self.comp="Car"

maruti=Car()
print(maruti.mil,maruti.comp,Car.wheel)
bmw=Car()
bmw.comp="BMW"
Car.wheel=55
print(bmw.mil,bmw.comp,bmw.wheel)
toyta=Car()
print(toyta.mil,toyta.comp,toyta.wheel)
