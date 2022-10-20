# while 문을 이용한 최대 공약수 구하기 프로그램

x = int(input("정수를 입력하시오 "))
y = int(input("정수를 입력하시오 "))

while(y!=0):
    r = x % y
    x, y = y, r #y는 x에 저장되고 r은 y에 저장된다 

print ("최대공약수는 "+ x+"입니다")

