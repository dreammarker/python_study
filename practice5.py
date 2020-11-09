#  -*- coding: utf-8 -*-
sentence = '나는 소년입니다'
print(sentence);
sentence2 = '파이썬은 쉬워요'
print(sentence2);
sentence3 = """나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
jumin = "990120-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 : "+jumin[:6])
print("뒤 7자리 : "+jumin[7:])
# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

print(python.find("Java")) # 원하는 값이 없을떈 -1
#print(python.index("Java")) # 오류가 나옴
print(python.count("n"))

print("나는 %d살입니다." %20)
print("나는 %s를 좋아해요" %"파이썬")

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20, color ="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color ="빨간", age =20))
# 
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 , {color}색을 좋아해요")
