data = []
f = open("C:\pythonfile\filetest.txt","r")

for line in f.readline():
    data.append(line.strip())


print(data)

