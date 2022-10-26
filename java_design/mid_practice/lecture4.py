# first class function
# 함수 자체를 인자로 다른 함수에 전달 
# 함수 자체를 다른 함수의 결과값으로 리턴
# 함수를 변수에 할당하거나 데이터 구조 안에 저장할 수 있는 함수 

def add(x):
    return x + x

print(add(5))

f = add

print(add)  # show same memory
print(f)    # show same memory

print(f(5))

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


num_list = [1,2,3,4,5]
adds = my_map(add,num_list)

print(adds) # just func parameterlist is func

# Closer 
# 일반 함수와 다르게, 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한 뒤, 
# 그 값을 엑세스 할 수 있도록 함
# 클로저 : 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가 함수를 호출 할 때
# 다시 꺼내서 사용하는 함수

# 지역 변수와 코드를 묶어서 사용하고 싶을 때 사용
# 클로저에 속한 지역 변수는 바깥에서 직접 접근 X 

def calc():
    a = 3 
    b = 5 
    def mul_add(x):
        return a * x + b # a = 3 , b = 5 저장 됩니다. 클로저 지원 
    return mul_add # 함수 자체를 반환, 호출 x

c = calc()

print(c(1),c(2),c(3))

del calc

print(c(1),c(2),c(3))





