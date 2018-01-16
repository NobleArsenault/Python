  # declare a class and give it name bike
class Bike(object):

    def __init__(self, price, max_speed,):

        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "price " + str(self.price)
        print "max speed " + str(self.max_speed)
        print "miles " + str(self.miles)
        return self

    def ride(self):
        print "riding..."
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "reversing..."
        self.miles = self.miles - 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(20000, "125mph")
bike1.ride().ride().ride().reverse().reverse().reverse().reverse().reverse().reverse().reverse().displayinfo()


