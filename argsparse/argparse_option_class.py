import argparse
import math


class Cat:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def __str__(self):
        return f'Cat(name={self.name}, color={self.color}, sound={self.sound})'    
    

    def lotto(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}인 고양이가 {self.sound}하고 운다.')






def parsing_argument():
    parser = argparse.ArgumentParser(description='Sample for using argparse',
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
   
    parser.add_argument(
       '-c',
       '--cat2',
       metavar="cat",
       type=str,
       nargs='*',
       help="assignment variables",
       default=["nabi", "white", "meow"]    
    )
    

    args = parser.parse_args()
    print(args)
    return args

parsing_argument()



def main():
  args = parsing_argument()
  cat = Cat(args.cat2[0],args.cat2[1],args.cat2[2]) 
  cat.lotto()




#   if args.title == "1":
#      name , color, sound = lotto(args.cat[0])
#      print({name}, {color}, {sound})
     
#   elif args.title == "2":
#     lotto(args.cat[0], args.cat[1], args.cat[2])



#   elif args.title == "No title":  
#      print("구하고자 하는 것이 없군")

main()
# parsing_argument()