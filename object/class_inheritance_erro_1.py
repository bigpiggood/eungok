# 클래스 상속

class Family:
    def __init__(self):
        self.lastname = "김" 
    def lname(self):
        print(f'성은 {self.lastname}')


class Person(Family):
    def __init__(self):
        self.firstname = "태경" 
    def fname(self):
        print(f'성은 {self.firstname}')


family = Family()
person = Person()        


family.lname()
person.lname()
person.fname()
person.lname()


# 아래는 오류를 잘보자, AttributeError: 'Person' object has no attribute 'lastname'. Did you mean: 'firstname'?
print(person.lastname)

