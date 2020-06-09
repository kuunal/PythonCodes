
def swap(nibbles):
    for index in range(0,4):
        nibbles[index], nibbles[index+4] = nibbles[index+4], nibbles[index]
    print(f'Swapped nibbles is {nibbles}')
    to_decimal(nibbles)

def to_decimal(nibbles):
    nibbles.reverse()
    decimal_value=0
    for power in range(len(nibbles)-1):
        decimal_value+=nibbles[power]*(2**power)
    print(decimal_value)

def main():
        
    nibbles=[]
    try:
        input_decimal_number = int(input("Enter number to find binary representation"))
    except ValueError:
        print("Invalid input!")
        main()
    else:
        print(input_decimal_number)
        while(input_decimal_number>0):
            nibbles.append(input_decimal_number%2)
            input_decimal_number = input_decimal_number//2
        if len(nibbles) < 8:
            pad = 8- len(nibbles)
            while(pad>0):
                nibbles.append(0)
                pad-=1
        nibbles.reverse()
        print(nibbles)
        swap(nibbles)

main()