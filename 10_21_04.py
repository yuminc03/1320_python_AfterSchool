from tkinter import *

def change_img():
    path=inputBox.get()
    img=PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image=img

window = Tk()  

photo=PhotoImage(file="afeach.gif")
imageLabel=Label(window, image=photo)
imageLabel.pack()

inputBox=Entry(window)
inputBox.pack()

button=Button(window, text="submit", command=change_img)
button.pack()

window.mainloop()

