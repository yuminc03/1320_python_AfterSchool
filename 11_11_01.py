# 클래스 선언 부분 ##
class Car :
 #color = ""
 name = ""
 speed = 0

 # def upSpeed(self, value) :
 #  self.speed += value
 #  if self.speed > 150 :
 #   self.speed = 150

 # def downSpeed(self, value):
 #  self.speed -= value

#생성자를 생성
 def __init__(self, name, speed):
  self.name = name
  self.speed = speed

 def getName(self):
     return self.name

 def getSpeed(self):
    return self.speed

 # def upSpeed(self, value):
 #  self.speed += value

 # def downSpeed(self, value):
 #  self.speed -= value

# 메인 코드 부분 ##
# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0

# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar1 = Car("빨강", 30)
# myCar2 = Car("파랑", 60)

#변수 선언 부분 ##
car1, car2 = None, None

#메인 코드 부분 ##
car1 = Car("아우디", 0)
car2 = Car("캡티바", 30)
print(" %s의 현재 속도는 %d km 입니다." % (car1.getName(), car1.getSpeed()))
print(" %s의 현재 속도는 %d km 입니다." % (car2.getName(), car2.getSpeed()))