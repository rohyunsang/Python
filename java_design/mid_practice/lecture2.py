# _single underscore
# 해당 클래스 또는 해당 클래스를 상속 받은 클래스에서만 접근 가능
# 해당 속성 , 함수 앞에 _(single underscore)

# __double underscore
# 해당 클래스에서만 접근 가능

# hasattr(a, x)

from os import access


class Calculate:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

a = Calculate(10,10)

#print(hasattr(a,x))
print(hasattr(a,'x'))

setattr(a,'x',20) # setter 
print(a.add()) #

class Person:
    def greeting(self):
        print('안녕하세요: 저는 parent class')

class Student(Person):
    def greeting(self):
        super().greeting() # sub class에서 parent class method call
        super().greeting()
        print('안녕하세요 저는 sub class')

student_1 = Student()
student_1.greeting()


# static method 란?
# 인스턴스화 하지 않고 메소드를 호출
# 독립적으로 사용하기 때문에 다른 속성에 접근 하거나 해당 클래스 내의 메소드를 호출 불가
# 메소드 위에 @staticmethod keyword

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20)
Calc.mul(10,20)

# class method 
# 인스턴스화 하지 않고 메소드를 호출
# 메소드 안에서 클래스의 다른 속성이나 클래스 메소드에 접근가능
# 메소드 위에 @classmethod 키워드 붙임

class PersonTwo:
    count = 0

    def __init__(self):
        PersonTwo.count +=1

    @classmethod
    def print_count(cls):
        print(cls.count , '명 생성되었습니다.')

    @classmethod
    def create(cls):
        p = cls()
        return p  #makit object


jason = PersonTwo()
jasonTwo = PersonTwo()
PersonTwo.print_count()
PersonTwo.create().print_count()
# PersonTwo.create() return value is object so we can use classmethod print_count




