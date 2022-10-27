from abc import *
from unicodedata import name

# component
class Node(metaclass = ABCMeta):
    def _init__(self):
        self.name = name

    @abstractmethod
    def print(self):
        pass


# leaf 
class File(Node):
    def __init__(self, name):
        self.name = name

    def print(self):
        print('파일 이름 : {}'.format(self.name))


# composite
class Directory(Node):
    def __init__(self,name):
        self.name = name
        self.nodes =[]

    def add(self,node):
        self.nodes.append(node)
    
    def remove(self,node):
        self.nodes.remove(node)

    def print(self):
        print('디렉토리 이름 : {}'.format(self.name))
        for node in self.nodes:
            node.print() # dictionary type object이면 self.print

directory = Directory('/')
directory.add(File('data1.txt'))
directory.add(File('data2.txt'))

directory2 = Directory('hello')
directory2.add(File('data3.txt')) # directory2(hello, data3.txt)
directory.add(directory2)

print('루트 디렉토리 출력')
directory.print()




