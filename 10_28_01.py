from tkinter import *

def update_add():
    update("add")
def update_sub():
    update("sub")
def update_reset():
    update("reset")
def update(method):
    
    global total 
    if method == "add":
        total += int(entry.get())
    elif method == "sub":
        total -= int(entry.get())
    else :
        total = 0
    sum['text'] = str(total)
    entry.dalete(0, END)

window = Tk()
total = 0

sum = Label(window)
sum.grid(row=0, column=1, columnspan=2)
   #0          1       2
#0 (현재합계)  (값)
#1 (Entry 박스(텍스트 박스))
#2  sumB      subB    resetB
label = Label(window, text="현재 합계: ")
label.grid(row=0, column=0)
entry = Entry(window)
entry.grid(row=1, column=0, columnspan=3)

add_button = Button(window, text="더하기(+)", command=update_add)
#command = 내가 불러 오고자 하는 함수명
subtract_button = Button(window, text="빼기(-)", command=update_sub)
reset_button = Button(window, text="초기화", command=update_reset)

add_button.grid(row=2, column=0)
subtract_button.grid(row=2, column=1)
reset_button.grid(row=2, column=2)
window.mainloop()
