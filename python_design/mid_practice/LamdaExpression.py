# def---가 아닌 간단한 식형태로 
# 이름 없는 함수, 익명 함수 라고도 함

def plus_ten(x):
    return x + 10

print(plus_ten(1))

# lambda x : x + 10

aa = lambda x : x + 10
print(aa(11))

print((lambda x : x + 10)(3)) # 호출 없이 람다식 자체를 바로 호출 가능 
# 람다식 안에서 변수를 만들 수 없음 

y = 10
print((lambda x  : x + y )(100))

# map 함수
# map(함수, 반복가능한 자료형), map 함수 반환값의 자료형은 map 객체 list 나 tuple 로 형 변환 
# 해주어야 함
# list(map (함수, 반복가능한 자료형))

myList = [1,2,3,4,5]

# for 반복문 이용

result1 = []
for i in myList:
    result1.append(i+10)

print('result1 : {}'.format(result1))

# map 함수 이용
result2 = list(map(plus_ten,myList)) # map 반환값을 list로 변환 
print('result2 : {}'.format(result2))

print('result3 :',list(map(lambda x : x + 10 ,myList)))

# result2 = list(map(plus_ten,myList))
# print('result 2 : {}'.format(result2))
# print('result3 :' list(map(lambda x : x + 10 ,myList)))

a = [1,2,3,4,5,6,7,8,9,10]

list(map(lambda x : str(x) if x % 3 == 0 else x, a))

a = [1,2,3,4,5]
b = [2,4,6,8,10]

list(map(lambda x, y : x * y , a, b))

# filter 함수 
# filter (함수, 반복가능한 자료형)
# 함수의 반환값이 True일 때만 해당 요소

def f(x):
    return x > 5 and x < 10 

a = [8,3,2,10,15,7,1,9,0,1]
list(filter(f,a))

print(list(filter(lambda x : x > 5 and x < 10 , a)))

