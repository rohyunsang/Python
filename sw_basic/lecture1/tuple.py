# tuple 제외 set, list, dictionary는 수정가능 
# list method 다 외우기 - 중간

from audioop import reverse


listA = [3,4,5,15,1,51,155,1]
listA.sort()
print(listA)


listA.reverse()
print(listA)

# shallow copy
# deep copy

a = (1)
print(a,type(a))

a = (1,)
print(a,type(a))
print(a[0])
# 콤마를 사용하면 괄호를 생략해도 튜플로 인식 : auto packing 


