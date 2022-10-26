def test_var_args(name, *args):
    print('첫 번째 인자',name)
    for arg in args:
        print('*argv의 다른 인자', arg)
        
test_var_args('000','2','222','11','111') # 다수의 파라미터를 튜플로 입력받음


def test_var_args(name, *args, **kwargs):
    print('첫 번째 인자',name)
    print(kwargs)
    for arg in args:
        print('*argv의 다른 인자', arg)
        
test_var_args('000','2','222',a = '111') # 함수에 키워드가 있는 가변 개수의 파라미터 입력 시 활용


# self 를 붙이지 않은 변수 해당 함수 내에서만 사용가능한 지역변수
# self 를 통해 선언해야만 외부에서 호출할 수 있고, 내부 함수에서 해당변수들을 사용할 수 있도록 해줌

class A:
    print('A')

class B(A): # inheritance 
    print('B')