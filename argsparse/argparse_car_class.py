import argparse
import math


class Car:
    def __init__(self, door, brand, color, rapid):
        self.door = door
        self.brand = brand
        self.color = color
        self.rapid = rapid


    def __str__(self):
        return f'Car(door={self.door}, brand={self.brand}, color={self.color}, rapid={self.rapid})'    


    def bigcar(self):
        print(f'자동차의 문짝은{self.door}, 브랜드는{self.brand}, 색상은{self.color}, 속도는{self.rapid}')


popo = Car("4", "은곡", "검정", "500")   
print(popo)


def parsing_argument():
    parser = argparse.ArgumentParser(description='Sample for using argparse',
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
   
    parser.add_argument(
       '-c',
       '--car',
       metavar="string",
       type=str,
       nargs='*',
       help="car car car car car",
       default=["4", "은곡", "검정", "500"]    
    )
    
    args = parser.parse_args()
    print(args)
    return args


# parsing_argument()


def main():
  args = parsing_argument()
  popopo = Car(args.car[0],args.car[1],args.car[2],args.car[3]) 
  popopo.bigcar()



main()
# parsing_argument()



