class StationaryGood():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getCost(self):
        pass
    
class Magazine(StationaryGood):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        
    def getCost(self):
        return self.price * self.quantity
    
class Book(StationaryGood):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def getCost(self):
        return self.price * self.quantity * 0.9

class Ribbon(StationaryGood):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def getCost(self):
        return self.price * self.quantity
    
basket = [ Magazine("Computer World", 70, 3), Book("Window 7 for Beginners", 200, 2), Ribbon("Blue ribbon", 5, 10)]

def getTotalCost(basket):
    totalcost = 0
    for com in basket:
        price = com.getCost()
        print(f"Name: {com.name} q:{com.quantity} -> price: {price}")
        totalcost += price
    print(f"Total cost: {totalcost} Bahts")
    
getTotalCost(basket)
        
        
        
        
