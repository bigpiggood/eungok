# 클래스 상속

class Family:
    lastname = '김'
    def lname(self):
        print(f'성은 {Family.lastname}')


class Person(Family):
    firstname = '태경'        
    def fname(self):
        print(f'이름은 {self.firstname}입니다.')


family = Family()
person = Person()        


family.lname()
person.fname()
person.lname()


# 아래는 오류를 잘보자
print(family.firstname)
print(family.fname)

