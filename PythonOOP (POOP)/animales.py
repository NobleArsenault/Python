class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def displayhealth(self):
        print(str(self.health)) 

class dog(animal):
    def __init__(self, name):
        super(dog, self).__init__(name, 150)
        print name 


class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name, 170)
    def displayhealth(self):
        print("im a dragon lol")
        super(dragon, self).displayhealth() 


animal1 = animal("cat", 190) 
animal1.displayhealth()

dragon1 = dragon("fire dragon")
dragon1.displayhealth()

dog1 = dog("jesus the dog")
dog1.displayhealth()







"""
class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

class Parent(object): # inherits from the object class
  # parent methods and attributes here
class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes
"""


"""
(splat operator)
allows you to input more than one argument 
  def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"

If we tested the type of args inside our function using type(args) we would get:

def varargs(arg1, *args):
   print "args is of " + str(type(args))
 varargs("one", "two", "three") # output: args is of <type 'tuple'>
"""