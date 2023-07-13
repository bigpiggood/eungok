
import math

def quadratic_equation_roots(a, b, c):
   if b ** 2 - 4*a*c < 0:
      print(f'실근이 없습니다.')
   else:
      x = b ** 2 - 4*a*c
      x1 = (-b + math.sqrt(x)) / (2*a)
      x2 = (-b - math.sqrt(x)) / (2*a)

      if b ** 2 - 4*a*c == 0:
        print(f'방정식의 해는 중근 {x1}입니다.')
      else:
         print(f'x1={x1} or x2={x2}')

a = int(input("이차항의 개수를 넣으세요"))
b = int(input("일차항의 개수를 넣으세요"))
c = int(input("상수항의 개수를 넣으세요"))

quadratic_equation_roots(a, b, c)


def circle(r):
   area = r ** 2 * math.pi
   round = r*2*math.pi

   return area, round
    

r = int(input("반지름을 입력해주세요."))

print(f'원의 넓이는{area}이고 둘레는{round}입니다.')

result = circle(r) 
print(result) 


# 배은아님 코드
def circle_square_round(a):
    square = a*a*math.pi
    round = 2*a*math.pi
    return square, round
a = int(input("반지름의 길이를 적으세요."))
square, round =circle_square_round(a)
print(f'square = {square}, round = {round}')



# 안지영님 코드
import math
def circle_3(a, b=math.pi):
    print(f'원의 넓이는 {a*a*b}이고, 원의 둘레의 길이는 {2*a*b}입니다.')

a = int(input("원의 반지름을 넣으세요"))
circle_3(a)



