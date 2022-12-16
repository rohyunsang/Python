from abc import * 

class Chef:
    def __init__(self,name):
        self.name = name
    
    def cook_spaghetti(self):
        print(f"{self.name}가 스파게티를 요리합니다")

    def cook_pizza(self):
        print(f"{self.name}가 피자를 요리합니다.")
        pass

class Watier:
    def __init__(self):
        self.orders = []

    def add_order(self,other):
        self.orders.append(order)
    
    def execute_orders(self):
        for order in self.orders:
            order.execute()
        self.orders = []

#Command
class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class SpaghettiOrder(Order):
    def __init__(self,chef):
        self.chef = chef
    
    def execute(self):
        self.chef.cook_spaghetti()

class PizzaOrder(Order):
    def __init__(self,chef):
        self.chef = chef

    def execute(self):
        self.chef.cook_pizza()

chef = Chef("고든램지")
waiter = Waiter()

order = SpaghettiOrder(chef=chef)
waiter.execute_orders()



