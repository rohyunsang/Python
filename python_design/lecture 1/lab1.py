print("안녕")  #design pattern은 조금만 한다.
# __init__ (__ double underscore) private

# getattr, setattr (getter,setter) 

# self keyword는 static method에서 쓰지 않는다. 
# 

print('안녕하세요 {} , ㅎㅇ{}'.format(10,20))

# 인스턴스 self, 
# cls는 class자체를 던져준다. 
# cls로 클래스 속성에 접근 , 현재 클래스를 뜻함 

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_cout(cls): # 매개변수 타입이 클래스
        # 클래스 메소드
        cls.name = 'jason'
        print(cls.name)
        print(cls.count)