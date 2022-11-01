import math

class Circle:
    '''A Circle instance models a circle with a radius'''
    def __init__(self,r = 1.0):
        self.radius = r

    def __repr__(self):
        '''Circle (r = 50.0)과 같은 형태로 Circle 표현'''
        return 'Circle(r='+str(self.radius)+')'

    def __str__(self):
        '''출력 형식 : This is a circle with radius of 50.00'''
        return "This is a circle with radius of " + str(self.radius)

    def get_area(self):
        return self.radius * self.radius * math.pi


c =Circle(50)
print(c) # __str__
print(repr(c))
print(c.get_area())