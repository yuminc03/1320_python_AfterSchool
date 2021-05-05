#클래스 선언 부분
# class Car :
#  color = "" #인스턴스 변수
#  speed = 0
#  count = 0

#  def __init__ (self) :
#   self.speed = 30
#   Car.count += 1

# myCar1, myCar2 = None, None

# ##메인 코드 부분 ##
# myCar1 = Car()
# myCar1.speed = 30
# print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대입니다." % (myCar1.speed, Car.count))

# myCar2 = Car()
# myCar2.speed = 60
# print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대입니다." % (myCar2.speed, myCar2.count))

#클래스 선언 부분 ##
class Car :
 speed = 0
 def upSpeed(self, value):
  self.speed += value

  print("현재 속도(슈퍼 클래스) : %d" % (self.speed))

class Sedan(Car):
   def upSpeed(self, value):
    self.speed += value

    if self.speed > 150:
      self.speed = 150

    print("현재 속도(서브 클래스) : %d" % (self.speed))

class Sonata(Sedan):
    pass

class Truck(Car):
    pass

#변수 선언 부분
sedan1, truck1, sonata = None, None, None

#메인 코드 부분
truck1 = Truck()
sedan1 = Sedan()
sonata = Sonata()

print("트럭 -->", end = "")
truck1.upSpeed(200)

print("승용차 -->", end = "")
sedan1.upSpeed(200)

print("소나타 -->", end = "")
sonata.upSpeed(200)