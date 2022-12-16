from abc import *

class AbstractClass(ABC):
    @abstractmethod
    def _required_operations1(self):
        pass

    @abstractmethod
    def _required_operations2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass

    def templete_method(self):
        self._required_operations1()
        self.hook1()
        self._required_operations2()
        self.hook2()

class ConcreteClass1(AbstractClass):
    def _required_operations1(self):
        print("ConcreteClass1 : Implemented Operation1")
    
    def _required_operations2(self):
        print("ConcreteClass2 : Implemented Operation2")
    
    def hook2(self):
        print("ConcreteClass1 : hook2")

concrete_logic = ConcreteClass1()
concrete_logic.templete_method()

# 후크 hook : 
# 서브클래스가 로직의 중간 단계를 제어할 수 있는 기능을 제공 
# 서브클래스는 Hook 를 사용하지 않아도 됨
# 서브클래스가 반드시 구현해야 하는 부분은 추상 메소드를 사용 

"""
템플릿 메소드의 목적
알고리즘 뼈대를 원시 연산으로 구현
알고리즘의 구조를 수정하지 않고 일부 서브클래스를 재정의
코드의 재사용과 중복 최소화
공통 인터페이스 및 구현 활용
사용 상황
여러 알고리즘 또는 클래스가 비슷하거나 같은 로직을 구현할 때
알고리즘을 단계별로 서브클래스화해서 코드의 중복을 줄일 수 있는 경우 
"""