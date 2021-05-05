'''
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

t=turtle.Turtle()
t.shape("turtle")
t.color("blue")

colors=["yellow", "red", "purple", "blue"]
for c in colors:
    t.color(c)
    t.forward(200)
    t.left(90)
'''
#for 반목문: 범위와 함께 사용하기
#for <범위 내부의 숫자를 담을 변수> in <범위>
#코드

#range() 함수로 반복해서 돌릴 때는 
#일반적으로 반복 변수를 한 문자로 인식해서
#출력한다.
'''
for i in range(10):#range = 범위
    print (str(i) + "번째 반복입니다.")

for i in range(5):
    print(str(i) + "반복 변수")
print()

for i in range(5, 10):
    print(str(i) + "반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "반복 변수")
print()

#리스트와 반복문 조합
array=[23,34,100,34,33]
for element in array:
    print(element)

array=[23,34,100,34,33]
for i in range(len(array)):
    print(array[i])
'''
#별 찍기
for i in range(5):
    for j in range(i+1):#참 일때 실행 함
        print("*", end=" ")#end 문장이 완성될 때까지
        #space로 해주겠다.
    print(" ")

print(" ")

#별 찍기2
for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print(" ")

#별 찍기3
for i in range(5):
    for j in range(4-i):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print(" ")
print(" ")

for i in range(5):
    for j in range(i):
        print(" ", end = " ")
    for k in range(5-i):
        print("*", end = " ")
    print(" ")