"""
상태 패턴 (State Pattern)
상태 자체를 객체화함으로써, 상태에 따른 액션도 상태 객체 내부에 구현하는 패턴 
보통 객체를 추상화할때.
행동의 주체 : 클래스 , 
대상이 하는 행동 : 메소드 , 
대상의 상태 : 속성
주체의 상태에 따른 행동이 다를 경우, 각 상태에 대한 조건문으로 대처함 
상태의 종류가 많아지면 조건문도 많아짐 => 코드 가독성 저하 
상태 자체를 객체로 만듦, 상태에 따른 액션도 객체에 포함 

- State : 객체의 행위를 캡슐화하는 인터페이스
- ConcreteState : state 인터페이스를 구현하는 서브클래스 특정 상태 객체에 대한 행위를 구현
- Context : 사용자가 선택한 인터페이스를 정의
            특정 상태를 구현한 ConcreteState 의 인스턴스를 가짐
"""

from abc import *

class State(metaclass = ABCMeta):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print('State A')

class ConcreteStateB(State):
    def handle(self):
        print('State B')

class Context:
    def __init__(self):
        self.state = None
    
    def setState(self,state):
        self.state = state

    def getState(self):
        return self.state

    def request(self):
        self.state.handle()

context = Context()
StateA = ConcreteStateA()
StateB = ConcreteStateB()
context.setState(StateA)
context.request()
context.setState(StateB)
context.request()

# 상태 패턴
# 장점  
# 새로운 형태를 쉽게 추가할 수 있음
# 상태 관련 행위가 ConcreteState 클래스에 있으므로 응집도 높아짐
# 새로운 ConcreteState 클래스를 추가해 쉽게 신규 기능 구현 
# => 코드 유연서 올라감, 유지보수 쉬움 
# 단점 
# => 클래스 남발 => 쓸데없는 클래스가 많아질 수 있음