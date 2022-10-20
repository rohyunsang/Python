class Television:

    serialNumber = 0 # 이것이 클래스 변수 

    def __init__(self,channel,volume,on):
        self.channel = channel
        self.volume = volume
        self.on = on

        Television.serialNumber += 1 #클래스 변수를 하나 증가한다 

    def show (self): # self 는 자기 자신을 참조하는 변수 
        print(self.channel,self.volume,self.on)

    def setChannel(self,channel):
        self.channel = channel
    
    def getChannel(self, channel):
        return self.channel

t = Television(9,10,True)
t.show()
t.setChannel(11)
t.show()