from abc import *
from locale import ABMON_1
from xml.dom.expatbuilder import parseFragmentString 

class 추상클래스이름(metaclass = ABCMeta):
    @abstractmethod
    def 메서드이름(self):
        self

class StudentBase(metaclass= ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하자')

# 추상 클래스는 인스턴스로 만들 수 없음
# -> 추상 메서드도 호출할 일 없음
# -> 추상 메서드도 내부 pass만 작성 

class AbstractCountry(metaclass = ABCMeta):
    name = '국가명'
    population = '인구'
    captial = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다')


a = AbstractCountry()

a.show() # 추상 클래스라 하더라도 추상 메소드가 없으면 기본적인 클래스 기능은 동작(객체 생성 가능)

class Animal(metaclass = AMCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("왈 왈 ")

class Cat(Animal):
    def do_say(self):
        print("야옹 야옹")

class ForestFactory(object):
    def make_sound(self,object_type):
        return eval(object_type)().do_say()

## client code
ff = ForestFactory()
animal = input("어떤 동물의 소리를 듣고 싶나요?")
ff.make_sound(animal)

# product의 세부 종류인 concreteProduct 객체의 생성을 creator의 자식 클래스인
# concreteCreator에서 담당하는 것 

# 팩토리 메서드 패턴 장점
# 특정 클래스에 구속되지 않기 때문에 개발 및 구현이 쉽다 
# ConcreteProduct가 아닌 인터페이스(Product)에 의존한다.

# 객체를 생성하는 코드가 이것을 활용하는 코드와 분리되어 있어 느슨한 결합을 이룬다.
# 클라이언트는 어떤 값을 보낼 지, 어떤 클래스를 생성해야 할지 신경 쓰지 않아도 된다.
# 새로운 클래스를 쉽게 추가할 수 있고, 유지보수가 쉽다.

# Product
class Mouse(metaclass = ABCMeta):
    @abstractmethod
    def click_left(self):
        pass

    @abstractmethod
    def click_right(self):
        pass

class G102(mouse):
    def click_left(self):
        print('click g102 left')
    
    def click_right(self):
        print('click g102 right')

class MagicMouse2(mouse):
    def click_left(self):
        print('magic mouse left')

    def click_right(self):
        print('magic mouse right')

# Factory
class MouseFactory(metaclass = ABCMeta):
    @abstractmethod
    def createMouse(self):
        pass

class LogiMouseFactory(MouseFactory):
    def createMouse(self):
        return G102

class AppleMouseFactory(MouseFactory):
    def createMouse(self):
        return MagicMouse2()


# Client
class Client():
    def use(self,company):

        if company =='logi':
            factory = LogiMouseFactory()
        elif company == 'apple':
            factory = AppleMouseFactory()
        else:
            return

        # create Product (make object)
        mymouse = factory.createMouse()
        # use instatiate product 
        mymouse.click_left()


# 서로 연관되거나 의존적인 객체들의 조합을 만드는 인터페이스를 제공하는 패턴,
# 관련성 있는 여러 종류의 객체를 일관된 방식으로 생성하는 경우에 유용

# 추상 팩토리 패턴 사용
# 객체가 생성되거나 구성, 표현되는 방식과 무관하게 시스템을 독립적으로 만들고자 할 때, ->
# -> 팩토리 패턴의 장점
# 여러 제품군 중 하나를 선택해서 시스템을 설정해야 하고 한번 구성한 제품을 다른 것으로 대체할 수 있을때
# 관련된 제품 객체들이 함께 사용되고 

        