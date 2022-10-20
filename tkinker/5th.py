from tkinter import *

window = Tk()

label = Label(window, text="안녕하셍?")
label2 = Label(window, text= "이것이 라벨 생성자")
label.pack()
label2.pack()
 

button = Button(window,text="thkinter로 버튼을 쉽게 만들 수 있습니다.")
button.pack()

window.mainloop()