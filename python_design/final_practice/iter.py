for i in range(3):
    print(i)

class MyIter:
    def __init__(self,end):
        self.current = 0 
        self.end = end

    def __iter__(self):
        return self

    def __next__(self): # python __next__ function must be return value variable
        if self.current < self.end:
            return value
        else :
            raise StopIteration

