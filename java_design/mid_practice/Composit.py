from abc import *

##component
class Node(metaclass=ABCMeta):
    def __init__(self):
        self.name

    @abstractmethod
    def print(self):
        pass

## leaf
class File(Node):
    def __init__(self,name):
        self.name = name

    def print(self):
        print(f'파일이름: {self.name}')


##composite
class Directory(Node):
    def __init__(self,name):
        self.name = name
        self.nodes = []

    def add(self,node):
        self.nodes.append(node)

    def remove(self,node):
        self.nodes.remove(node)

    def print(self):
        print(f'디렉토리 이름: {self.name}')
        for node in self.nodes:
            node.print()

directory = Directory('/') # directory name 
directory.add(File('data1.txt'))
directory.add(File('data2.txt'))

directory2 = Directory('hello')
directory2.add(File('data3.txt'))
directory.add(directory2)


print('루트 디렉토리 출력')
directory.print()


