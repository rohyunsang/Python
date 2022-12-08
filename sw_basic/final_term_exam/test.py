class student:

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.id = "32181395"

    def __str__(self):
        return 'name {0} number {1} id {2}'.format(self.name,self.number,self.id)


a = student("노윤상",'01039489077')
print(a)

infile = opern("test.txt","r")
for line in infile :
    line = line.rstrip() #오른쪽 공백 문자를 제거
    print(line)
infile.close()

