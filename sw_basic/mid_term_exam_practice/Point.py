from typing import Counter


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __del__(self):
        print("Point :" , self, "이 삭제되었습니다.")

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5  

    def __str__(self):
        return "x = %d, y = %d " %(self.x,self.y)
    
    def halfway(self,target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx,my) # return Object 

p = Point(3,5)
q = Point(5,3)
mid = p.halfway(q) # instanciate object mid 
    


# a = Counter() => Counter.__init__(a)

