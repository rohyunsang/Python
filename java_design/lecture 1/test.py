from abc import *
# Product
class Animal(metaclass = ABCMeta): # 추상 클래스 선언
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("왈 왈")

class Cat(Animal):
    def do_say(self):
        print("야옹 야옹!!")

class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

ff = ForestFactory()
animal = input("Dog or Cat")
ff.make_sound(animal)