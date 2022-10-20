class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)

v = Vector2D(0,1)
u = Vector2D(1,0)

a = v + u 
print(a)

#지역 변수 - 함수 안에서 선언되는 변수
#전역 변수 - 함수 외부에서 선언되는 변수
#인스턴스 변수 - 클래스 안에 선언된 변수, 앞에 self.가 붙는다 

#클래스는 속성과 동작으로 이루어진다. 속성은 인스턴스 변수로 표현되고 동작은 메소드로 표현된다.
#객체를 생성하려면 생성자 메소드를 호출한다. 생성자 메소드는 __init__() 이름의 메소드이다.
#인스턴스 변수를 정의하려면 생성자 메소드 안에서 self.변수이름과 같이 생성한다. 