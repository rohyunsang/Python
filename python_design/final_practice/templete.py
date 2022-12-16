from abc import *
class AbstractClass(ABC):
    #로직의 요소
    @abstractmethod
    def _requried_operations1(self):
        pass

    @abstractmethod
    def _requried_operations2(self):
        pass

    def template_method(self):
        self._requried_operations1()
        self._requried_operations2()


class ConcreteClass1(AbstractClass):
    
    def _requried_operations1(self):
        print("ConcreteClass1 : Implemented Operation1")

    def _requried_operations2(self):
        print("ConcreteClass2 : Implemented Operation2")
        
class ConcreteClass2(AbstractClass):
    
    def _requried_operations1(self):
        print("ConcreteClass1 : Implemented Operation1")

    def _requried_operations2(self):
        print("ConcreteClass2 : Implemented Operation2")

    
concrete_logic = ConcreteClass1()
concrete_logic.template_method()

concrete_logic = ConcreteClass2()
concrete_logic.template_method()