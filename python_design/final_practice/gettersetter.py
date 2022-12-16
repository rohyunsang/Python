# @property
# 파이썬의 접근 제어자 
# 클래스의 인스턴스의 내부 데이터를 보호하기 위해서 데이터의 접근용 메서드를 작성 (getter, setter)

class Person:
    def __init__(self):
        self.__age = 0

    def getter(self):
        return self.__age
    
    def setter(self,age):
        self.__age = age

    @property
    def full_name(self):
        return self.__first_name + " " + self.__last_name


jason = Person()
jason.setter

