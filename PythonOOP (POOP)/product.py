class Product(object):
    def __init__(self, itemName, price, weight, brand):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "SOLD!"
        print str(self.status)
        return self

        
    def addtax(self):
        self.price = self.price + (int(self.price) * 0.15)
        print "$ " + str(self.price)
        return self

    def returnItem(self, reason):
        if reason == "Defective":
            self.price = 0 
            self.status = "Defective"
            print self.itemName
            print self.price
            print self.weight
            print self.brand
            print self.status
        if reason == "Like New":
            self.status = "for sale"
            print self.itemName
            print self.price
            print self.weight
            print self.brand
            print self.status

        if reason == "Used":
            self.price = self.price - (int(self.price) * 0.20)
            print self.itemName
            print self.price
            print self.weight
            print self.brand
            print self.status
        
        return self


object1 = Product("Designer Tomato", 10.00, 3.5, "gucci")
object1.returnItem("Used")
object2 = Product("Designer Pickle", 27.99, "7lb", "Louis Vuitton")
object2.sell().addtax().returnItem("Defective")