from tkinter import *

class App:
    def __initf__(self):
        window = Tk()
        helloB = Button(window,text="hello",command=self.hello,fg = "red")
        helloB.pack(side=LEFT)
        quitB = Button(window, text="Quit",command=self.quit)
        quitB.pack(side=LEFT)
        window.mainloop()

    def hello(self):
        print("Hello 버튼이 클릭되었음")

    def quit(self):
        print("Quit 버튼이 클릭되었음")

App()
