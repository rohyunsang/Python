import math

value = abs(-100)


for x in range (1, 4):
    print(value)

# 함수의 정의
def fun_name (parameter,parameter2):
    print(parameter)
    print(parameter2)


def get_sum(start,end):
    sum = 0
    for i in range(start,end):
        sum += i
    return sum 


print(get_sum(1,11))

#function call 

def square(n):
    return n*n

print (square(100))

# def main(): main() 정의 

def sphereVolume(radius):
    volume = (4.0/3.0) * math.pi * radius * radius * radius
    return volume


radius = float(input('구의 반지름을 입력하시오: '))
print(sphereVolume(radius))


