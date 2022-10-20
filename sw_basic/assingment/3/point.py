from re import X


class Point:
    def __init__(self,name,x,y):
        self.__name = name
        self.__x = x
        self.__y = y


    def __del__(self): # auto called using del method
        print('Point : x =',self.__x,', y =',self.__y,'이 삭제되었습니다.')

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def distanceFormOrigin(self):
        return (self.__x**2 +self.__y**2)**0.5

    def halfway(self,other):
        return int((self.__x + other.getX()) / 2) , int((self.__y + other.getY()) /2)

    def __str__(self):
        print (self.__name,': x =',self.__x,', y =',self.__y)

    
p = Point('p',3,4)
q = Point('q',5,12)

midX,midY = p.halfway(q)
mid = Point('mid',midX,midY)

p.__str__()
q.__str__()
mid.__str__()
print(p)
print(q)
print(mid)

del (mid)

