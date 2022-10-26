# 인스턴스가 단 하나만 생성되는 것을 보장하고 어디서나 그 인스턴스에 접근가능 하기 위함

# 목적 : 클래스에 대한 단일 객체 생성
# 전역 객체 제공

# Ex : 계산기 클래스를 만들고, 여러 파일에 있는 코드에서 필요할 때마다 객체로 불러서 계산
# 매번 계산할 때마다, 객체를 새로 만들 필요 없음
# 객체 생성시 마다 메모리를 차지하므로, 불필요한 객체 생성 시간, 메모리 사용률 절약

class SingleTon():
    def __new__(cls):
        if not hasattr(cls,'instance'): # cls 안에 instance 가 없으면
            print('make instance') # instance를 만든다. 
            cls.instance = super().__new__(cls) # cls.instance = super.__new__(cls)
            # cls.instance : class 의 instance 변수는 객체
        return cls.instance



s1 = SingleTon()
print( 'Object created ', s1) # two objects have same memory space 
s2 = SingleTon()
print( 'Object created ', s2) # two objects have same memory space 


#SingleTon Pattern Example Two

class DbCheck:
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

print(hc1)
print(hc2)

hc1.addServer()
print(hc1._servers)

hc2.changeServer()
print(hc1._servers)
