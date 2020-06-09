

def func(f):
    def inner_method(msg):
        x=""
        while type(x) is not int: 
            try:
                x= int(input(msg))
                return x
            except ValueError:
                print("Please enter valid input!")
    return inner_method

@func
def take_input(msg):
    return x
