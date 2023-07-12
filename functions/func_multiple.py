# a, b, c 매개변수
def multiple(a, b, c):
    num = a*b*c
    return num


a = 5
b = 5
c = 5

# a, b, c 위치인자로 전달
result = multiple(a, b, c)
print(result)