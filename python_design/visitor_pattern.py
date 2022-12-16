# 방문자와 방문공간을 분리하여 방문 공간이 방문자를 
# 맞이할 떄, 이후에 대한 행동을 방문자에게 위임하는 패턴

# 방문공간이 방문자를 입력 받은 후, 방문자의 행동을 호출 함
# 이때, 방문공간의 정보를 파라미터로 넘겨줌

# Visitor
# 방문자 클래스의 추상 클래스(인터페이스)
# visit(Component) 보유, Component는 방문 공간
# Component

# 방문 공간 클래스의 추상 클래스(인터페이스)
# accepy(Visitor)보유 (내부적으로 Visitor.visit(this)), Visitor는 방문자
# ConcreteVisitor : Visitor를 구체적으로 구현한 클래스
# ConcreteComponent : Component를 구현한 클래스

from abc import *

class Component(ABC):
    @abstractmethod
    def accept(self,visitor):
        pass

class ConcreteComponentA(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_a(self)

    def method_of_concrete_component_a(self):
        return 'A'

class ConcreteComponentB(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_b(self)
    
    def method_of_concrete_component_b(self):
        return "B"

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self,concrete_component_a):
        pass

    @abstractmethod
    def visit_concrete_component_b(self,concrete_component_b):
        pass

class ConcreteVisitor(Visitor):
    def visit_concrete_component_a(self, concrete_component_a):
        print(f"{component.method_of_concrete_component_a()}+ConcreteVisitor1")

    def visit_concrete_component_b(self, concrete_component_b):
        print("{} + ConcreteVisitor1".format(component.method_of_concrete_component_b()))

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, concrete_component_a):
        print(f"{component.method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, concrete_component_b):
        print("{} + ConcreteVisitor2".format(component.method_of_concrete_component_b()))

component = [ConcreteComponentA(), ConcreteComponentB()]

visitor1 = ConcreteVisitor()
for component in components:
    component.accept(visitor1)