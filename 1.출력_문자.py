#기본 출력 방법
print("# 하나만 출력합니다. ")
print("hello python")
print()

print("#여러개를 출력합니다. ")
print("'10, 20, 30, 40, 50")
print("안녕","저의","이름은","추유민입니다.")
print('안녕',"저의","이름은","추유민입니다.")

#이스케이프 문자
# point('안녕','반가워')
# point("안녕", "반가워")

# \ " " : 큰 따옴표를 의미하는 이스케이프 문자
print("\"안녕하세요 \" 말했다.")
print('\'안녕하세요 \' 말했다.')

# \t탭을 의미하는 의미하는 이스케이프 문자
print("이름\t나이\t지역")
print("추유민\t20\t서울")

# \\ : \를 나타내는 이스케이프 문자
print("// // // ")
print() 
print()
print()

#문자열 연결 연산자
print("hi" + "...!")

# a<문자열>*<숫자> : 반복적 의미를 가진다.
print("안녕" * 3)
# print("안녕" + 3) : 허용하지않는다.

#문자 선택 연산자 : <문자열> [<숫자>]
print("안녕하세요." [0])
print("안녕하세요." [-5])
print()
print()

#문자열 범위 선택 연산자 : <문자열> [<숫자>:<숫자>] 
#[0:2]라고 입력하면 뒤의 숫자 번째가 선택되지 않는다.
#즉, 0번째 글자부터 1번째 글자를 선택하는 것이다.
print("안녕하세요."[0:2])
print("감사합니다."[1:4])
print("사랑합니다."[0:3])
print("고맙습니다."[2:4])