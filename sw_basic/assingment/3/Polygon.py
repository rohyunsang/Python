import math

class Polygon:

    p_num = 0

    def __init__(self,side,n):
        self.side = side
        self.n = n
        Polygon.p_num = Polygon.p_num + 1
    
    def __str__(self):
        print('한 변의 길이 ' , self.side,'인',self.n,'각형')
    
    def __del__(self):
        Polygon.p_num = Polygon.p_num - 1
        print('한 변의 길이 ' , self.side,'인',self.n,'각형 삭제')

    def internal_angle(self):
        return (self.n - 2)/self.n * 180
    
    def area(self):
        return (self.n * self.side) / (4 * math.tan(3.14/self.n))
    
angle_3 = Polygon(50,3)
angle_5 = Polygon(10,5)

angle_3.__str__()
print('면적 : ', angle_3.area()) # 면적이 교수님과 다르게 나옵니다. ㅜ
print('내각 : ', angle_3.internal_angle())

angle_5.__str__()
print('면적 : ', angle_5.area())
print('내각 : ', angle_5.internal_angle())

print('생성된 정다각형의 개수 : ' ,Polygon.p_num)

del (angle_3)