a = 10
b = "Hello"

print(type(a))
print(type(b))



a = True
print(type(a))




a = b = c = 10
d, e, f = 10, 3.14, "test"

print(a, b, c)
print(d, e, f)


str = "안녕하세요!!! '김태경'"
str_literal = """
fdfsdfsdfssdfdsf \n
fdfsdfsdfssdfdsf \n
fdfsdfsdfssdfdsf \n
"""


print(str)
print(str_literal)


# 리터럴 표기 방법

name = "김태경"
literal_1 = "안녕하세요!!!" + "    " +  name + " sfeee"
print(literal_1)


literal_2 = f"안녕하세요!!!   {name}     fefefefe"
print(literal_2)

print(3 == 3 and 3>5)
print(3 == 3 & 3>5)

print(3==3 or 3>5)
print(3==3 | 3>5)

print(not False)
print(~False)

print(not 3>5)

