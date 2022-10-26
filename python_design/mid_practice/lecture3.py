from abc import *

class AbstractClass(metaclass = ABCMeta):
    @abstractmethod
    def AbstractMethod():
        pass

class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하자')
    def go_to_school(self):
        return super().go_to_school()

student_a = Student()
# checking implements all abstractmethods when is you making object

class AbstractCountry(metaclass = ABCMeta):
    name = '국가명'
    population = '인구'

    def show(self):
        print('추상 국가 클래스의 메소드입니다.')

a = AbstractCountry()
a.show()  # 추상 클래스라 할지라도 추상 메소드가 없으면 기본적인 클래스 기능은 동작 (객체 생성 가능)


# 팩토리 메서드 : 객체 생성 메소드를 클라이언트에 노출
# 추상 팩토리 메서드 : 연관된 객체들의 패밀리 생성을 위한 하나 이상의 팩토리 메소드를 포함

# 팩토리 메서드 : 하나의 product를 만들기 위해 사용됨
# 추상 팩토리 메서드 : 연관된 product들의 패밀리를 생성하는 것 