# def keyword_함수(**kwargs):
#     print(type(kwargs))
#     num = 0
#     print(kwargs.values())

#     for i in kwargs.values:
#         num +=i


#     return num    
# result = keyword_함수(a=1, b=5, c=3)
# print(result)


def name_hello_함수(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # for i in kwargs:
    #     print(type(i))
    #     print(f'{kwargs[i]} 님 안녕하세요!!')

    for i in kwargs.values:
        # print(type(i))
        print(f'{i} 님 안녕하세요!!')

      
# name_hello_함수(a="김태경", b="김태뽕", c="김태발")
