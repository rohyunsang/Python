import Bird
from Bird import Parrot
from Bird import Penguin

lulu = Parrot(10)
chichi = Penguin(10)
print(lulu.__repr__())
lulu.fly()
print(chichi.__repr__())
chichi.fly()