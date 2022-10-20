import math

# tuple은 list와 아주 유사하다. 
colors = ("a","b","c","d")
print(colors) #tuple도 list와 마찬가로 여러 가지 자료형의 값을 섞어서 생성할 수 있다.
t = (10,) # tuple은 ,(콤마)도 넣어야 한다. 쉼표가 없으면 단순한 수식으로 처리한다. (10)은 정수 10이나 마찬가지이다.

def calCircle():
    area = math.pi * r * r
    circum = 2 * math.pi * r

radius = float(input("원의 반지름을 입력하시오"))
(a,c) = calCircle(radius)
print("원의 넓이는 " + str(a)+ "이고 원의 둘레는 "+str(c)+"이다")


