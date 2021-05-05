#if 구문
'''
number = input("<정수 입력>")
number = int(number)
if(number > 0):
    print("양수")
else:
    print("음수")

숫자를 압력받아서 짝수/홀수 판별
num = int(input("정수를 입력하세요 :"))
 if num%2 == 0 :
     print("짝수입니다.")
 else:
     print("홀수입니다.")

import datetime 
now = datetime.datetime.now()
month = now.month
if 3<=month<=5:
    print("봄입니다.")
elif 6<=month<=8:
    print("여름입니다.")
elif 9<=month<=11:
    print("가을입니다.")
else:
    print("겨울입니다.")

1. 점수를 입력받는다.
-점수는 실수 타입으로 입력받을 수 있다.
2. 입력받은 점수가 4.2이상 ~ 4.5미만
-아주잘했어요~!
3. 입력받은 점수가 3.5이상 ~ 4.2미만
-잘했어요~
4. 입력받은 점수가 2.8이상 ~ 3.5미만
- 조금 더 노력하세요~
5. 나머지는
- 노력하세요~
score = float(input("(실수)점수를 입력하세요 : "))
if 4.5>score>=4.2 :
    print("아주잘했어요~!")
elif 4.2>score>=3.5 :
    print("잘했어요~")
elif 3.5>score>=2.8 :
    print("조금 더 노력하세요~")
else:
    print("노력하세요~")
'''
#리스트 선언하기
array=[263,12,13,"문자",True]
print(array)
print(array[0])
print(array[3])
print(array[1:3])
array[0] = "변경"
print(array[0])
print(array[-1])
print(array[-2])
#리스트 연산자
list_a=[1,2,3]
list_b=[4,5,6]
print("list_a + list_b = ",list_a+list_b)
print("list_a * 3 = ",list_a*3)
print("len(list_a) = ",len(list_a))
list_a.append(4)
list_a.append(5)
print(list_a)
print("len(list_a) = ",len(list_a))
list_a.insert(0,10)
print(list_a)
del list_a[1]
print(list_a)
del list_a[1:3]
print(list_a)

array=[273,32,103,57,52]
for element in array:
    print(element)
for char in "안녕하세요":
    print("-", char)

#딕셔너리

dictionary={
    "name" : "건조망고",
    "type" : "당절임",
    "origin" : "필리핀"
}
print(dictionary)

print("name:",dictionary["name"])
dictionary["name"]="건조 파인애플"
print(dictionary)