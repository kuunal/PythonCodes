import decorators
def validate(input_year):
    if len(str(input_year)) != 4:
        raise Exception("Invalid year! Please enter year of 4 digits.");


def check_leap_year(input_year):
    return input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0)

try:
    input_year = int(input("Enter year to find out leap or not"))
except ValueError:
    print("Please enter year in numbers!")    
else:
    validate(input_year)
    is_leap_year = check_leap_year(input_year)
    print(input_year, " is leap year!" if is_leap_year else "is not a leap year!")
