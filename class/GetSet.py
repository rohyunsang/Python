class Student:
    def __init__(self, name = None , age = 0):
        self.__name = name
        self.__age = age 

    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age == age
    '''
    def setAge(self,age):
        if(age<0):
            self.__age = 0 
        else:
            self.__age = age 
    setter 설정자 사용예시 
    
    '''
    def setName(self,name):
        self.__name = name


obj = Student("Hong",20)
obj.getName()

#접근자와 설정자의 사용 이유
#접근자와 설정자를 사용해야만 나중에 클래스를 업그레이드할 때 편하다.
#접근자에서 매개 변수를 통하여 잘못된 값이 넘어오는 경우, 이를 사전에 차단할 수 있다.
#필요하 때마다 인스턴스 변수값을 계산하여 반화할 수 있다.
#접근자만을 제공하면 자동적으로 읽기만 가능한 인스턴스 벼수를 만들 수 있다. 

