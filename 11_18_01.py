from tkinter import *
import time
import random

class Ball:
 def __init__(self,canvas, color, size, x, y, xspeed, yspeed):
  self.canvas=canvas
  self.color=color
  self.size=size
  self.x=x
  self.y=y
  self.xspeed=xspeed
  self.yspeed=yspeed
  self.id=canvas.create_oval(x,y,x+size,y+size,fill=color) #canvas에 원을 그린다, (x,y)에서 (x+size, y+size)의 크기를 가진다
  #fill은 배경색깔

 def move(self):
  self.canvas.move(self.id, self.xspeed, self.yspeed)
  (x1,y1,x2,y2)=self.canvas.coords(self.id) #coords = 좌표값을 감지 원이 창의 끝에 닿으면 멈추도록 코드를 짬
  (self.x,self.y)=(x1,y1)
  if x1 <= 0 or x2 > WIDTH:
      self.xspeed =- self.xspeed
  if y1 <= 0 or y2 > HEIGHT:
      self.yspeed =- self.yspeed


WIDTH=800
HEIGHT=400

window=Tk()
canvas=Canvas(window,width=WIDTH, height=HEIGHT)
canvas.pack() #원을 삽입
color_list=["yellow","red","green","blue","pink","gray","skyblue","black"]
balls_list=[]

for i in range(10):
 color=random.choice(color_list)#color_list안의 색깔을 무작위로 뽑는다
 size=random.randrange(10,100)# 윈도우 창을 업데이트한다
 xspeed=random.randrange(1,10)
 yspeed=random.randrange(1,10)
 balls_list.append(Ball(canvas,color,size,0,0,xspeed,yspeed))

# ballA=Ball(canvas,"red",30,0,0,10,0)
# ballB=Ball(canvas,"yellow",30,0,0,0,10)

while True:
 # ballA.move()
 # ballB.move()
 for ball in balls_list:
  ball.move()
 window.update()
 time.sleep(0.03)#속도(숫자가 작을 수록 빠름
 window.update()
 time.sleep(0.03)

'''
ballA=Ball("red", 30,0,0,0,0)
print("공의 색상",ballA.color)
print("공의 크기",ballA.size)
print("공의 x좌표",ballA.x)

ballB=Ball("blue",100,50,50,10,10)
print("공의 색상",ballB.color)
print("공의 크기",ballB.size)
print("공의 x좌표",ballB.x)
'''