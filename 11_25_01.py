from tkinter import *
import time

WIDTH=800
HEIGHT=400

class Ball:
  def __init__(self,canvas,color,size,x,y,xspeed,yspeed):
    self.canvas=canvas
    self.color=color
    self.size=size
    self.x=x
    self.y=y
    self.xspeed=xspeed
    self.yspeed=yspeed
    self.id=canvas.create_oval(x,y,x+size,y+size,fill=color) #canvas에 원을 만듦

  def move(self):
    self.canvas.move(self.id, self.xspeed, self.yspeed)
    (x1,y1,x2,y2)=self.canvas.coords(self.id)
    (self.x,self.y)=(x1,y1)

    if x1 <= 0 or x2 > WIDTH:
        self.xspeed =- self.xspeed
    if y1 <= 0 or y2 > HEIGHT:
        self.yspeed =- self.yspeed

bullets=[] 
def fire(event): #총알 메서드
    bullets.append(Ball(canvas,"red",10,150,250,10,0))

def getScore(score):
    score = score+1
    return score

window = Tk()
canvas=Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>",fire)
score=0
var=StringVar() # string값을 위한 메서드
label=Label(window, textvariable=var, relief="solid") #실선타입의 라벨형 구성

spaceship=Ball(canvas,"green",100,100,200,0,0)
enemy=Ball(canvas,"red",100,500,200,0,5)

while True: 
    var.set("score : " + str(score))
    label.pack()

    for bullet in bullets:
        bullet.move() 
        #총알이 화면을 벗어나면 삭제한다.
        if(bullet.x+bullet.size)>=WIDTH: 
            canvas.delete(bullet.id)
            bullets.remove(bullet)
            #적을 맞추면 점수가 올라간다
        if bullet.x > enemy.x and bullet.x < enemy.x+enemy.size and bullet.y > enemy.y and bullet.y < enemy.y+enemy.size:
               score = getScore(score)

    enemy.move()
    window.update()
    time.sleep(0.03)