name = 'Dankook Best'

print(repr(name)) # 'Dankook Best'
print(str(name))  # Dankook Best

a = eval(repr(name)) # 객체를 재생산
print(type(a)) # <class 'str'>
print(a) # Dankook Best

#b = eval(str(name)) 객체를 재생산 하지 못함

num = 1000
print(repr(num))
print(str(num))

num1 = eval(repr(num))
num2 = eval(str(num))

print(type(num1)) # <class 'int'>
print(type(num2)) # <class 'int'>

class DKU:
    def __repr__(self):
        #instance를 생성할때와 동일한 표현을 하면 재생산가능(re-create) 가능
        return 'DKU()'
    def __str__(self):
        return '단국'

a = DKU()
print(a)
print(str(a))
print(repr(a))

print('%s' %a)
print('%r' %a)

print(eval(repr(a)))
#print(eval(str(a)))

obj = eval(repr(a))
print(type(obj))
