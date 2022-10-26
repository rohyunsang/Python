# 객체를 생성하는 팩토리 클래스를 정의
# 어떤 객체를 만들지는 팩토리 객체에서 결정하여 객체를 만들도록 하는 패턴

# 팩토리 패턴 : 심플 팩토리, 팩토리 메서드, 추상 팩토리

# 팩토리 패턴 장점
# 클래스의 구현과 객체 생성이 독립적 -> 상호 의존도를 줄임
# 클라이언트가 객체를 생성하는 클래스를 알 필요가 없음(메소드,파라미터,인터페이스만 알면됨)
# 클라이언트가 코드를 수정하지 않아도 다른 타입의 객체를 생성하기 위한 클래스 추가가 쉬움

from abc import *

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print('wal wal')
    
class Cat(Animal):
    def do_say(self):
        print('nyang nyang')

# Core Code
class ForestFactory(object):
    def make_sound(self,object_type):
        return eval(object_type)().do_say() 
        # eval(obejct_type)().do_say()
        # run => object_type().do_say()
        # Cat().do_say()

ff = ForestFactory()
animal = input("어떤 동물")
ff.make_sound(animal)
Cat().do_say()
Dog().do_say()
a = Dog()
a.do_say()

