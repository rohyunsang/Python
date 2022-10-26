# 프로토타입 패턴은 기존의 객체를 복사하여 새로운 객체를 만들고 복사한 객체를 변경하여 사용하는 패턴
# 복사된 객체를 프로토타입이라고 함 

# shallow copy, deep copy
# python에서는 copy 라이브러리에 deepcopy() 함수로 간단하게 프로토타입 패턴 지원

# import copy
# object2 = copy.deepcopy(object1)

import copy
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 0

    def set_z(self):
        self.z = 18

p1 = Point(1,2)
p1.set_z()

p2 = copy.deepcopy(p1) # copy.deepcopy

print(p2.x)
print(p2.y)

p2.x = 6
p2.y = 7

print(p2.x)
print(p2.y)

print(p2.z)