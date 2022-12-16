# 전략 패턴은 행동/전략 등 동일계열의 알고리즘들을 캡슐화 하고 알고리즘들을 위임형태로 가지는 패턴

# context 
# 클라이언트가 직접 사용하는 클래스
# Strategy 인터페이스를 위임

# strategy 구체적인 알고리즘들의 공통 스펙을 정의하는 클래스
# concreteStrategy 구체적인 알고리즘들을 구현하는 클래스

from abc import *

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self,data):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


class Context():
    def __init__(self,strategy):
        self.__strategy = strategy
    
    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self,strategy):
        self.__strategy =strategy
    
    def do_some_logic(self):
        result = self.__strategy.do_algorithm(["a","b","c","d","e"])
        print(",".join(result))


context = Context(ConcreteStrategyA())
context.do_some_logic()

context = Context(ConcreteStrategyB())
context.do_some_logic()

# 전략 패턴(Strategy Pattern)
# 장점 
# 상황에 따라 사용할 알고리즘을 쉽게 바꿀 수 있음
# 알고리즘 구현부와 사용부가 분리되어 있음
# Strategy를 활용해서 사용자는 일관성 있게 알고리즘을
# 가져다 쓸 수 있음

# 단점
# 구체적인 알고리즘마다 필요한 입력 파라미터가 다를 수 있음
# Strategy 에 파라미터가 고정되어 있으므로 알고리즘에 필요없는 파라미터도 받게 됨

# 활용 상황 
# 상황에 따라 사용해야 할 알고리즘을 클라이언트가 정할 때
# 동일 계열의 알고리즘들을 인터페이스로 통일하여 제공해야 할 때
