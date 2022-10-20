class Box:

    def __init__(self,width,length,height):
        self.width = width
        self.length = length
        self.height = height

    def setWidth(self,width):
        self.width = width

    def setLength(self,length):
        self.length = length

    def setHeight(self,height):
        self.height = height

    def getWidth(self):
        return self.width
        
    def getLength(self):
        return self.length

    def getHeight(self):
        return self.height

    def getBoxVolume(self):
        return self.height * self.length * self.height

box = Box(10,20,30)

print(box.getWidth(),box.getLength(),box.getHeight())
print("넓이는 " , box.getBoxVolume())


