import math

class Polygon:
    p_num = 0  # class variable

    def __init__(self,x = 1, size = 3):
        self.side = x
        self.n = size
        Polygon.p_num += 1 

    def __del__(self):
        Polygon.p_num -= 1
        print(self,'삭제')

    def __str__(self):
        return '한 변의 길이 %d인 %d각형' %(self.side,self.n) # % 앞에 , 가 없다.

    def area(self):
        area = (self.n * self.side**2) / 4 * math.tan(3.14/self.n)
        return area 

    def internal_angle(self):
        return ((self.n-2)/self.n) * 180

a = Polygon(50,3)
b = Polygon(10,5)

print(a)
print('면적',a.area()) 
print('내각',a.internal_angle())
print()
print(b)
print('면적:',b.area())
print('내각:',b.internal_angle())
print()

print('생성된 정다각형의 개수:',Polygon.p_num)
print()
del a

