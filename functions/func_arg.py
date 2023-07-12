# a, b, c 매개변수
def multipl_add(aa, bb, cc):
    num = aa*bb+cc
    return num


# a, b, c 위치인자로 전달
result = multipl_add(2, 3, 4)
print(result)


# a, b, c를 키워드 인자로 전달
result_keywords = multipl_add(aa=2, bb=3, cc=4)
print(result_keywords)

# 키워드 인자는 위치를 바꿔도 된다...
result_keywords_1 = multipl_add(cc=4, aa=2, bb=3)
print(result_keywords_1)


# 위치인자부터 먼저 호출하고 나중에 키워드 인자를 호출한다.
result_keywords_2 = multipl_add(2, 3, cc=4)
print(result_keywords_2)

# 매개변수 키워드값을 부여하면 인자값으로 전달받지 않아도 된다.
def multipl_add_keywords(aa, bb, cc=100):
    num = aa*bb+cc
    return num


result_1 = multipl_add_keywords(10, 20)
print(result_1)

result_2 = multipl_add_keywords(10, 20, 500)
print(result_2)

result_3 = multipl_add_keywords(cc=10, aa=20, bb=500)
print(result_3)

result_4 = multipl_add_keywords(aa=20, bb=500)
print(result_4)