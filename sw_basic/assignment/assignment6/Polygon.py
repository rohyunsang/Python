class Polygon:
    def __init__(self,no_of_size):
        self.n = no_of_size
        self.sides = [0 for i in range(no_of_size)]

    def inputSides(self):
        self.sides = [float(input("Enter side " ,str(i+1)+":")) for i in range (self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangel(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a,b,c = self.sides
        # cal the semi perameter

        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of the triangle is %0.2f" %area)


t = Triangel()
t.inputSides()
t.dispSides()
t.findArea()


#Enter side 1:3
#Enter side 2:4
#Enter side 3:5
#Side 1 is 3.0
#Side 2 is 4.0
#Side 3 is 5.0
#The area of the triangle is 6.00


