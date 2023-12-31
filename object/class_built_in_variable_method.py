class MagicMethod:
    area = 0

    def __add__(self, other):
        return self.area + other.area
    
    def __lt__(self, other):
        return self.area < other.area


    def __le__(self, other):
        return len(self.area) >= len(other.area) 
    
    def __ne__(self, other):
        return len(self.area) != len(other.area)

    def __eq__(self, other):
        return len(self.area) == len(other.area)


a = MagicMethod()    
a.area = 10
b = MagicMethod()
b.area = 20

# print(a+b)
# print(a.__add__(b))
a.area = "hello"
b.area = "hellow world"
print(a.__lt__(b))
print(a.__le__(b))
print(a.__ne__(b))


a.area = "hello"
b.area = "hello"
print(a.__eq__(b))

print(dir(int))