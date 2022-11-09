class MultipleOfN:

    currentCount = 1

    def __init__(self,n,stop):
        self.n = n
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.n * self.currentCount <= self.stop :
            result = self.n * self.currentCount
            self.currentCount += 1
            return result
        else:
            raise StopIteration

for i in MultipleOfN(3,30):
    print(i)

