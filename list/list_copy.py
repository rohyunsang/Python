# list copy : 리스트 변수는 리스트 객체를 직접 저장하고 있지 않다. 리스트의 참조값(reference)만 변수에 저장된다. 참조값이란 메모리에서 리스트 객체의 위치이다.
# 결론부터 말하자면 리스트는 복사되지 않는다. scores와 values는 모두 동일한 리스트 객체를 가리키고 있다. 이것을 얕은 복사 swallow copy라고 한다.

# list를 올바르게 복사하려면 깊은 복사 deep copy 를 해야한다 여러 가지 방법이 있다. 
# first : list() 메소드를 사용하는 것이다.

from ast import Expression
from copy import deepcopy


scores = [10,20,30,40,50]
values = list(scores)
values[2] = 99
print(scores)
print(values)

# second : deepcopy() 메소드를 사용하는 방법도 있다. 
# from copy import deepcopy
scores2 = [10,20,30,40,50]
values2 = deepcopy(scores2)

# 값으로 호출하기 call by value
# 참조로 호출하기 call by reference

# 파이썬에서는 정수나 문자열처럼 변경이 불가능한 객체들은 "값으로 호출하기" 방법으로 전달된다.
# 객체의 참조값이 함수의 매개 변수로 전달되지만 함수 안에서 객체의 값을 변경하면 새로운 객체가 생성되기 때문이다.

def func1(x):
    print("x=",x,"id = ",id(x))
    x = 42
    print("x=",x,"id = ",id(x))

y = 10 

print("y=",y,"id=",id(y))
func1(y)
print("y=",y,"id=",id(y))

# 우리가 변경가능한 객체인 리스트를 함수에 전달하면 어떻게 될까?
# 리스트는 참조값으로 전달된다. 리스트는 함수 안에서 변경할 수 있다. 

def func2(list):
    list[0] = 99

values = [0,1,2,3,4,5,6]
print(values)
func2(values)
print(values)

# 파이썬은 리스트 함축을 지우너한다 .list comprehensions or 리스트 컴프리핸션 

S = [ x**2 for x in range(10)] #python is range boundary [x,y)

print(S)

# default structure : [ expression for i in old_list if filter(i)]

new_list = []
for i in old_list:
    if filter(i):
        new_list.append(Expression(i))



list1 = [3,4,5]
list2 = [x*2 for x in list1]
print(list2) #Console : 6 8 10 

# list comprehension example
new_list = []
for x in range(1,30):
    for y in range(x,30):
        for z in range(y,30):
            if x**2 + y**2 == z**2:
                new_list.append((x,y,z))

print(new_list)


