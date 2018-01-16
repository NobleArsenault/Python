class Car(object):

    def __init__(self, name, price, speed, fuel, mileage):
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else: 
            self.tax = 0.12

    def displayall(self):
        print "Name: " + str(self.name)
        print "Price " + str(self.price)
        print "Speed " + str(self.speed)
        print "Fuel " + str(self.fuel)
        print "Mileage " + str(self.mileage)
        print "Tax " + str(self.tax)
        return self


car1 = Car("Fiat", 11111, "125mph", "full", "20mpg")
car2 = Car("Audi",11666, "169mph", "full", "66mpg")
car3 = Car("Maserati", 33666, "201mph", "full", "100mpg")
car4 = Car("car #4", 2666, "100mph", "full", "12mpg")
car5 = Car("Smart Car", 9000, "110mph", "full", "27mpg")
car6 = Car("Civic", 600, "55mph", "half", "8mpg")
car1.displayall()
car2.displayall()
car3.displayall()
car4.displayall()
car5.displayall()
car6.displayall()