# from tkinter import * 

# window=Tk() #윈도우 창(컨테이너) 생성, 창 이름 = Tk
# button=Button(window, text = "클릭하세요.")#윈도우 창에 "클릭하세요" 버튼 만들기
# button.pack()#화면에 배치(나타나게) 함
# window.mainloop()#이벤트 감지 상태로 만듦

#하나의 버튼이 있는 윈도우를 생성해보자
# from tkinter import *

# window = Tk()
# l1=Label(window, text = "화씨")
# l2=Label(window, text = "섭씨")
# l1.pack()
# l2.pack()

# e1=Entry(window)
# e2=Entry(window)
# e1.pack()
# e2.pack()

# b1=Button(window,text="화씨->섭씨", bg="red")
# b2=Button(window,text="섭씨->화씨", bg="yellow")
# b1.pack()
# b2.pack()
# window.mainloop()

#배치관리자 격자(grid)
# from tkinter import *

# window = Tk()
# l1=Label(window, text = "화씨")
# l2=Label(window, text = "섭씨")
# l1.grid(row=0, column=0)
# l2.grid(row=1, column=0)

# e1=Entry(window)
# e2=Entry(window)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# b1=Button(window,text="화씨->섭씨", bg="skyblue")
# b2=Button(window,text="섭씨->화씨", bg="pink")
# b1.grid(row=2, column=0)
# b2.grid(row=2, column=1)
# window.mainloop()

from tkinter import *

def process():
    #e2.insert(0, "100") #엔트리 위젯의 0번째 위치에 
                        #"100"을 추가
    temperature=float(e1.get())
    mytemp=(temperature-32)*5/9
    e2.insert(0, str(mytemp))

def process1():
    temperature2=float(e2.get())
    mytemp2=(temperature2+32)/5*9
    e1.insurt(0, str(mytemp2))

window = Tk()
l1=Label(window, text = "화씨")
l2=Label(window, text = "섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1=Entry(window, bg="orange", fg="white")
e2=Entry(window, bg="orange", fg="blue")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1=Button(window,text="화씨->섭씨", bg="skyblue", command=process)
b2=Button(window,text="섭씨->화씨", bg="pink", command=process1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
window.mainloop()