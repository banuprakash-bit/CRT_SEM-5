'''from math import pi 
class circle:
    r =7
    count = 0 
    def __init__(self):
        self.count += 1
    def area(self):
        return pi * self.r * self.r
    def perimeter(self):
        return 2 * pi * self.r
c1= circle(7)
c2= circle(10)
c3= circle(15)
print(c1.area())
print(c1.perimeter())    
print(c2.area())
print(c2.perimeter())   
print(c3.area())
print(c3.perimeter())     

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big 
        self.medium = medium
        self.small = small

        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0 :
                self.big -= 1
                return True
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small > 0 :
                self.small -= 1
                return True
        return False                        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
'''