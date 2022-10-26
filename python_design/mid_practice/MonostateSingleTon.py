# Monostate SingleTon Pattern
# 싱글톤 패턴에 의하면 클래스의 객체는 하나만 존재하여야 함
# 일부 개발자들은 객체 생성 여부 보다
# 객체의 상태, 행위가 더 중요하다고 주장
# 모노스테이트는 모든 객체가 같은 상태를 공유함

class Monostate:
    __share_state = {"a":13}
    def __init__(self):
        self.__dict__ = self.__share_state

b1 = Monostate()
b2 = Monostate()

print(b1.a)
print(b2.a)

b1.a = 15
print(b1.a)
print(b2.a)

# they share same memory 

# SingleTon Pettern 단점 :
# 전역 변수의 값이 실수로 변경된 것을 모르고 사용될 수 있음
# 한 개의 객체만을 만들기 때문에 같은 객체에 대한 여러개의 참조자가 생김
# 전역 변수를 수정하면 종속된 모든 클래스에 의도하지 않은 영향을 줄 수 있음 

