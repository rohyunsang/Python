def logger(msg):
    def log_message():
        print('Log: ',msg)


    return log_message

log_hi = logger('Hi')  #

print(log_hi)

log_hi() # Hi 값이 logger 함수가 종료된 이후에도 참조
# log_message 함수를 closer 라고 부름
# 클로저는 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억 할 수 있음 

del logger 

log_hi() # logger을 지워도 msg가 저장돼어 있다. 

