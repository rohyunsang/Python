# 서로 연관되거나 의존적인 객체들의 조합을 만드는 인터페이스를 제공하는 패턴
# 여러 종류의 객체들을 일관된 방식으로 생성하는 경우에 유용 

from abc import *
from locale import ABMON_1
# (abstract) Product

class Keyboard(metaclass = ABCMeta):
    @abstractmethod
    def type_words(self):
        pass

class Mouse(metaclass = ABCMeta):
    @abstractmethod
    def type_words(self):
        pass

# diff factory method pattern this codes

# (abstract)Factory
class ComputerFactory(metaclass=ABCMeta):
    @abstractmethod
    def createKeyBoard(self):
        pass

    @abstractmethod
    def createMouse(self):
        pass

# FactoryMethod Pattern 은 Mouse Factory 하나로 2개 만들었지만
# AbstractFactory Pattern 은 Mouse, KeyBoard 하나씩 추상 메소드 만들어짐 
# 연관된 제품 생산 가능



    
