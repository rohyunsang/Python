#OOP object oriented programming 

#객체 안의 변수를 인스턴스 변수 
#객체를 클래스의 인스턴스
#정수 객체 안에 구현되어 있는 add()
#공용 인터페이스만 제공하고 구현 세부 사항을 감추는 것을 캡슐화
#class Car:
#    def add(self):
    
#    def min(self): # 이들은 클래스의 멤버 


class Counter :
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count


a = Counter()

a.reset()
a.increment()
print("카운터 a의 값은 " , a.get())
