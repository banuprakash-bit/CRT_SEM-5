'''
from math import pi 
class circle:
    r =7 
    def area(self):
        return pi * self.r * self.r
    def perimeter(self):
        return 2 * pi * self.r
c= circle()
print(c.area())
print(c.perimeter())    
'''