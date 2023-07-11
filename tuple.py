# t1 = ()
# t2 = (1,)
# t3 = (1, 2, 3)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))


# # print(type(t2))
# print(t5[2])
# print(t5[2][0])



# indexing
# t1 = (1, 2, 'a', 'b')
# print(t1[2])

# slicing

# t1 = (1, 2, 'a', 'b', 'c')
# print(t1[1:])

tu = (5, 2, 10, 4, 7, 9)

# 2, 10, 4
print(tu[1:4]) 

# 5 ~ 7
print(tu[:5])

# 10 ~ 
print(tu[2:])

# 4, 7
print(tu[-3:-1])



# 원소의 갯수
# print(len(tu))

# for i in range(len(tu)):
#     print("Hello!!")
#     print(tu[i])


# tuple 더하기
# t1 = (1, 2, 'a', 'b')
# t2 = (3, 4)
# # t3 = t1 + t2
# # (1, 2, 'a', 'b', 3, 4) 
# # print(t3)

# # tuple 곱하기
# t3 = t1 * 2

# print(t3)

# print(tuple([1,2,3]))
# print(list([1,2,3]))