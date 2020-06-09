import decorators
import math

def main():
    
  
    print("Enter three values")
    a = decorators.take_input("Enter value of a")
    b = decorators.take_input("Enter value of b")
    c = decorators.take_input("Enter value of c")
    delta = b*b-(4*a*c)
    try:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
    except ValueError:
        print("Wrong values provided!")
    else:    
        print(x1,x2)

main()