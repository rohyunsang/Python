class Singleton:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            print('make instance')
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Singleton()
print('Object created',s1)

s2 = Singleton()
print('Object created',s2) # same memory

# 싱글톤 패턴에 의하면 클래스의 객체는 하나만 존재해야 함

class Monostate:
    __shared_state = {"a":13} #dictionary = { 키1 : 값1 }
    def __init__(self):
        self.__dict__ = self.__shared_state
        #__dict__ 클래스의 인스턴스 변수와 값을 딕셔너리로 가지고 있음

b1 = Monostate()
b2 = Monostate()

print(b1.a) 
print(b2.a)

# Console : 13 13
b1.a = 44
print(b1.a)
print(b2.a)

# Console : 44 44

print("b1",b1)
print("b2",b2)

# 다른 메모리를 가지는 객체지만 같은 속성(변수)를 공유함 

# 파이썬 __dict__ 의 용도 : 클래스 객체의 속성 정보를 확인하기 위해 사용 객체가 가진 여러가지 속성들을 
# 딕셔너리 형태로 편하게 확인할 수 있다.

class DbCheck :
    _instance = None
    def __new__(cls):
        if not DbCheck._instance:
            DbCheck._instance = super().__new__(cls)
        return DbCheck._instance

    def __init__(self):
        self._servers = []
    
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = DbCheck()
hc2 = DbCheck()

print('hc1',hc1)

hc1.addServer()
print(hc1._servers)

print("Schedule DB check for servers (1)...")
for i in range(4):
    print("Checking ",hc1._servers[i])

hc2.changeServer()

print("Schedule DB check for servers (2)...")
for i in range(4):
    print("Checking ",hc2._servers[i])