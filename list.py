# # a = []
# # b = [1, 2, 3]
# # c = ['Life', 'is', 'too', 'short']
# # d = [1, 2, 'Life', 'is']
# # e = [1, 2, ('Life', 'is')]



# # # 리스트 슬라이싱
# # a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# # a[2:5]
# # [3, ['a', 'b', 'c'], 4]
# # a[3][:2]
# # ['a', 'b']



# # # 리스트 더하기
# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # a + b
# # [1, 2, 3, 4, 5, 6]

# # # 리스트 반복하기
# # a = [1, 2, 3]
# # a * 3
# # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# # # 리스트 값 수정하기
# # a = [1, 2, 3]
# # a[2] = 10
# # print(a)


# # # del 함수를 활용해서 리스트 값 삭제하기
# # a = [1, 2, 3]
# # del a[1]

# # print(a)
# # [1, 3]


# # remove 함수를 활용해서 리스트 값 삭제하기
# # b = [1, 2, 3, 1, 2, 3]

# # b.remove(3)
# # print(b)

# # b.remove(3)
# # print(b)

# # pop 활용해서 리스트 요소 끄집어 내서 삭제
# c = [1, 2, "ㅁ"]
# c.pop(1)
# print(c.pop())


# # append 리스트에 요소 추가하기
# d = [1, 2, 3]
# d.append(4)
# print(d)


# # insert 리스트에 요소 삽입
# a = [1, 2, 3]
# a.insert(0, 4)
# a
# print(4)
# [4, 1, 2, 3]

# # extend()
# nums = [1, 2, 3]
# nums.extend([4])
# nums.extend(['a','b'])
# print(nums)


# # sort(*, key=None, reverse=False)
# # sorted(iterable, /, *, key=None, reverse=False)
a = ["b", "a"]
b = [5, 2, 3, 1, 4] 
c = sorted(["b","a","c"], reverse=True)

# a.sort()
# b.sort()
# print(a)
# print(b)
# print(c)

# a.sort(revers=True)
# print(c)





# key

# '''정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.

# # key 값을 기준으로 정렬되고 기본값은 오름차순이다'''

str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))


# revers

a = ['a', 'c', 'b']
f = [1, 2, 'a', 'c', 'b' ]
g = [1, 2, 3, 'a', 'b', 'c']

a.reverse()
print(a)
f.reverse()
print(f)
f.reverse()
print(f)


# index 반환
a = [1, 2, 3]
a.index(3)
2
a.index(1)
0
print(a.index(2))

# count 함수
a = [1, 1, 1, 2, 3]
print(a.count(1))

# clear 함수
a = [1, 1, 1, 2, 3]
a.clear()
print(a)

# 원소 추가
a.append(5)
print(a)

# 리스트 추가
a.extend([3,4])
print(a)

a.append([3, 4])
print(a)

a.insert(0, "뿜뿜")
print(a)


