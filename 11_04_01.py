# from turtle import *
# #거북이 움직이기

# alex = Turtle()

# alex.forward(100)
# alex.left(90)
# alex.forward(200)


class Car:
  def __init__(self, speed, color, model):
   #init = 초기화
   self.speed = speed
   self.color = color
   self.model = model

   def drive(self):
      self.speed = 60

myCar = Car(0, "blue", "E-class")

print("자동차 객체를 생성하였습니다.")
print("자옹차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동타의 모델은", myCar.model)
print("자동차를 주행합니다.")
myCar.drive()
print("자동차의 속도는", myCar.speed)