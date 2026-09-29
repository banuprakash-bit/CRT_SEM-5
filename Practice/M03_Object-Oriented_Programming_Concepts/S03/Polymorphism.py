'''
Polymorphism:
poly ==> many
marph ==> forms

types of polymorphoism:
1. compile-time
    1. function overloading - 
    2. operation overloading
2. run-time:
    1. method overridding    

print(10+20)
print("abc"+"xyz")


# funtion overloading
def add(a+b):
    return a + b
def add(a,b,c):
    return a+b+c
def add(a,b,c,d):
     return a+b+c+d
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))


pytjon does not support function overloading directly we can achive this using variable-length arguments(using *)

def add(*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
'''
'''
#operator overloading
class a:
    def __init__(self,x):
        self.x = x
    def __add__(self,val):
        return self.x + val.x
    def __it__(self,val):
        return self.x < val.x
    def __sub(self,val):
        return self.x - val.x


a = a(10)
b = a(20)
print(a + b) 
print(a - b)   
print(a < b)
'''
'''
#example:
class B:
     def __init__(self,x,y):
            self.x = x
            self.y = y
     def __add__(self,val):
          return (self.x + val.x, self.y + val.y)
     def __sub__(self, val):
          return (self.x - val.x, self.y - val.y)
a = B(10,20)
b = B(30,40)
print( a + b)
print( a - b)

# method overriding: Same method name in parent and child class, but the child gives a different implementation.
class parent:
      def display(self):
            print("parent class display method")

class child:
      def display(self):
            print("child class display method")
c = child()
c.display()
parent.display(c) 


# duck typing
class Dog:
      def sounds(self):
            print("bark")
class cat:
      def sounds(self):
            print("meow")
def make_sound(animal):
      animal.sounds()

make_sound(Dog())
make_sound(cat())                              



'''






















