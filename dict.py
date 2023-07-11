# immutable 예
a = {"a" : 1, "b":2}
# print(a)
# immutable 예
a1 = {1: 5, 2: 3}   # int 사용
print(a1)
{1: 5, 2: 3}
a2 = {(1,5): 5, (3,3): 3} # tuple사용
print(a2)
{(1, 5): 5, (3, 3): 3}
a3 = { 3.6: 5, "abc": 3} # float 사용
print(a3)
{3.6: 5, 'abc': 3}
a4 = { True: 5, "abc": 3} # bool 사용
print(a4)
{True: 5, 'abc': 3}



print({"a" : 1, "a":2})


print(a2[(1,5)])

# keys(), values(), items() 키값과 밸류값을 리스트로 출력
print(a.keys())
print(a.values())
print(a.items())


# 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
d = {'abc': 1, 'def': 2}
d['ssdfsfdffdfd'] = 10
d['abc'] = 55

print(d)

# dict 만들기
result = dict([('a', 1), ('b', 2), ('c', 3)])
print(result)


newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
print(newdict)
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}


# dictionary변환
name_and_ages = [['alice', 5], ['Bob', 13]]
dict(name_and_ages)
{'alice': 5, 'Bob': 13}
name_and_ages = [('alice', 5), ('Bob', 13)]
dict(name_and_ages)
{'alice': 5, 'Bob': 13}
name_and_ages = (('alice', 5), ('Bob', 13))
dict(name_and_ages)
{'alice': 5, 'Bob': 13}
name_and_ages = (['alice', 5], ['Bob', 13])
dict(name_and_ages)
{'alice': 5, 'Bob': 13}

# 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({'bob':99, 'tony':99, 'kim': 30})
print(a)

# dictionary(딕셔너리) for문
# 키값 호출
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for i in a:
    print(i)

# 밸류값 호출
for j in a.values():
    print(j)

# 키/밸류값 모두 호출
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for k in a.items():    
    print(k)


key_list = []
value_list = []

for x, y in a.items():
    key_list.append(x)
    value_list.append(y)

print(key_list)    
print(value_list)












