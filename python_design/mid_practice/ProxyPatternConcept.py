# 일반적으로 프록시란 요청자와 공급자 사이의 중재자를 말함.
# 어떤 객체를 사용할 때 객체를 직접적으로 참조하는 것이 아닌 
# 해당 객체를 대리하는 객체를 통해서 대상 객체에 접근하는 방식

# 장점 : 원래 객체에 대한 접근 제한 및 제어
#      : 메모리 사용량이 큰 객체가 로딩 전에 프록시를 통해서 참조 가능

# 단점 : 객체 생성에 한 단계를 거치므로 빈번한 객체 생성 시 성능 저하 
# 발생 가능 ,  코드 가독성 저하

# 프록시 패턴의 종류 
# 가상 프록시 : 생성하기 힘든 자원에 대한 접근 제어
#            : 클라이언트가 객체를 처음 요청하거나 접근 했을 때 실객체 생성
# 원격 프록시 : 원격 객체에 대한 접근 제어
#            : 원격 서버나 다른 주소공간의 객체를 로컬 인스턴스로 생성
# 보호 프록시 : 접근 권한이 필요한 자원에 대한 접근 제어 
