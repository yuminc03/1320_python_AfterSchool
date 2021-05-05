from tkinter import *

def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() == 2:
        labelImage.configure(image = photo2)
    else :
        labelImage.configure(image = photo3)
    #if value가 1 이면,
    #강아지 이미지 보이게
    #elif value가 2 이면,
    #고양이 이미지 보이게
    #else 토끼 이미지

#전역 변수 선언 부분
var, labelImage = 0, None
#None = 자료형(아무것도 없다, 아무것도 저장하지 않겠다.)
photo1, photo2, photo3 = [None]*3

#메인 코드 부분
if __name__ == "__main__" :
    #main일 때만 name을 수행함.
    window = Tk()
    window.geometry("400x400") #윈도우의 사이즈 지정
    window.title("애완동물 선택하기")
    Labeltext=Label(window, text="좋아하는 동물 투표 ", fg="blue", font=("궁서체", 20))

    var = IntVar()
    rb1=Radiobutton(window, text="강아지", variable=var, value=1) #var = 그룹
    rb2=Radiobutton(window, text="고양이", variable=var, value=2)
    rb3=Radiobutton(window, text="토끼", variable=var, value=3)
    buttonOk=Button(window, text="사진보기", command=myFunc)

    photo1 = PhotoImage(file = "image/dog2.gif")
    photo2 = PhotoImage(file = "image/cat2.gif")
    photo3 = PhotoImage(file = "image/rabbit2.gif")

    labelImage = Label(window, width = 200, height = 200, bg = "yellow", 
     image = None)
     #이미지를 보여줌.
    Labeltext.pack(padx = 5, pady = 5)
    rb1.pack(padx = 5, pady = 5)
    rb2.pack(padx = 5, pady = 5)
    rb3.pack(padx = 5, pady = 5)
    buttonOk.pack(padx = 5, pady = 5)
    labelImage.pack(padx = 5, pady = 5)

    window.mainloop()

