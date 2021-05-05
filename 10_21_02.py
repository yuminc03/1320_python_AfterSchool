from tkinter import *

def process(): #def = 정의하다
    print("안녕하세요.")

window=Tk()
button=Button(window, text="클릭", command=process)
button.pack()
window.mainloop()