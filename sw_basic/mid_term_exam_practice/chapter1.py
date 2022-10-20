# is : 메모리 비교
# == : 값 비교

a = '대한민국만세'

print(a[::-1])

print('대' in a) #True
print('영' in a) #False

# python에서 변수는 단지 객체의 이름
# 심볼 테이블 : 변수의 이름과 데이터의 주소를 저장하는 테이블
# 네임 스페이스 : 객체에 대한 이름과의 매핑관계를 포함하고 있는 공간
class foo:
    goo = 'hello'
    print(goo) # access symbol table

print(foo.goo) # access namespace