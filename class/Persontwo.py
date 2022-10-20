from tkinter.font import names


class Person:
    def __init__(self,name,email,num_car):
        self.name = name
        self.email = email
        self.num_car = num_car

    def print_info(self):
        print("==========Person=======")
        print("name", self.name)
        print("email",self.email)
        print("num_car",self.num_car)
        print("==========Person=======")


a = Person("A","B",1)
a.print_info() # not run => cuz didnt call print function 