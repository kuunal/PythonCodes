import random
from employee_error import EmployeeWageError


class Companies:
    total_wage = 0
    daily_wage = [] 

    def __init__(self, COMPANY_NAME, WAGE_PER_HOUR, FULL_DAY_HOUR, MONTHLY_WORKING_DAY, TOTOL_WORKING_HOURS):
        self.WAGE_PER_HOUR = WAGE_PER_HOUR,
        self.FULL_DAY_HOUR = FULL_DAY_HOUR,
        self.MONTHLY_WORKING_DAY = MONTHLY_WORKING_DAY,
        self.TOTOL_WORKING_HOURS =  TOTOL_WORKING_HOURS,
        self.COMPANY_NAME = COMPANY_NAME 
           
    def get_company_name(self):
        return self.COMPANY_NAME

    def get_wage_per_hour(self):
        return int(self.WAGE_PER_HOUR[0])
    
    def get_full_day_hour(self):
        return int(self.FULL_DAY_HOUR[0])
    
    def get_total_working_hours(self):
        return int(self.TOTOL_WORKING_HOURS[0])

    def get_monthly_days(self):
        return int(self.MONTHLY_WORKING_DAY[0])

    def total_and_daily_wage(self, total_wage=0, daily_wage=[0]):
        self.total_wage=total_wage
        self.daily_wage=daily_wage

    def get_total_wage_and_daily_wage(self):
        total_daily_wage_dict = {0 if self.total_wage==0 else self.total_wage:self.daily_wage}
        return total_daily_wage_dict

class Employee:
    # constant = Constant()
    switcher = {}
    company_list=[]

    # checks attendance of employee and returns wage according to attendance
    def check_employee(self,wage_per_hour, full_day_hour):
        random_attendance = round(random.randint(0,2))
        self.switcher = {
            0 : self.calculate_fullday_wage(wage_per_hour, full_day_hour ),
            1 : self.calculate_fullday_wage(wage_per_hour, full_day_hour )//2,
            2 : 0
        }
        return self.switcher.get(random_attendance)

    # calculates and returns full day wage
    def calculate_fullday_wage(self, wage_per_hour, full_day_hour):
        return wage_per_hour * full_day_hour

    # calcaluates wage till certain days or hours and returns wage
    def calculate_wage_till_total_hour_or_days(self, company_name, wage_per_hour, full_day_hour, monthly_working_day, total_working_hours):
        daily_wage=[]
        hours = total_working_hours
        days = monthly_working_day
        total_wage = 0
        while hours > 0 and days > 0:
            wage = self.check_employee(wage_per_hour,full_day_hour)
            daily_wage.append(wage)
            total_wage += wage
            if(wage == self.calculate_fullday_wage(wage_per_hour,full_day_hour)):
                hours -= full_day_hour
            elif(wage == self.calculate_fullday_wage(wage_per_hour,full_day_hour)//2):
                hours -= full_day_hour//2
            else:
                pass
            days -= 1
        [company for company in self.company_list if company.get_company_name()==company_name][0].total_and_daily_wage(total_wage,daily_wage)
        return total_wage

    def main(self):
        while True:
            print("1.ADD \n 2.Remove \n 3.List all companies \n 4.Enter company to get total and daily wage \n 5.Exit")
            try:
                choice = int(input("Enter choice"))
            except ValueError:
                print("Invalid option! Please choose proper option.")
                self.main()
            else:
                menu_dict= {
                    1: self.add_company,
                    2: self.remove_company,
                    3: self.print_companies,
                    4: self.get_total_and_daily_wage_of_company,
                    5: exit 
                    }
                func = menu_dict.get(choice)
                func()

    # takes user input to get total and daily wage of company 
    def get_total_and_daily_wage_of_company(self):
        try:
            if len(self.company_list) == 0:
                raise EmployeeWageError("No companies registered yet!")
        except EmployeeWageError as e:
            print("No companies registered yet!")
            self.main()
        company_name = input("Enter company name")
        self.get_company_to_calculate_details(company_name)
    
    # gets all details of company required to calculate total and daily wages
    def get_company_to_calculate_details(self,company_name):
        try:
            company = [company for company in self.company_list if company.get_company_name()==company_name][0]
        except IndexError:
            print("No such company registered!")
            self.main()
        else:
            wage_info = company.get_total_wage_and_daily_wage()
            calculated_total = [keys for keys in wage_info.keys()][0]
            if calculated_total == 0:
                self.calculate_wage_till_total_hour_or_days(company_name, company.get_wage_per_hour(), company.get_full_day_hour(), company.get_monthly_days(), company.get_total_working_hours())
            self.print_total_and_daily_wage(wage_info,company_name)

    # prints calculated total and daily wage
    def print_total_and_daily_wage(self, wage_info,company_name):
        for total_wage, dailywage_list in wage_info.items():
            if total_wage != 0:
                print(f'Total wage :{total_wage} for company :{company_name}')
                for day,dailywage in enumerate(dailywage_list):
                    print(f'daily wage: {dailywage} for day: {day}')

    # add new company by adding it onto list
    def add_company(self):
        company_name = input("Enter name of company")       
        try:
            if [company for company in self.company_list if company.get_company_name() == company_name]:
                raise EmployeeWageError("Company already registered!")
            wage_per_hour = int(input("Enter Wage per hour"))
            full_day_hour = int(input("Enter working hour in full day"))
            monthly_working_day = int(input("Enter monthly working day"))
            total_working_days = int(input("Enter total working days"))
        except ValueError:
            print("invalid details! Please Enter again.")
            self.add_company()
        except EmployeeWageError as e:
            print(str(e))
        else:
            self.company_list.append(Companies(company_name, wage_per_hour, full_day_hour, 
            monthly_working_day, total_working_days))
            self.get_company_to_calculate_details(company_name)

    # removes existing company from the list
    def remove_company(self):
        try:
            if len(self.company_list) == 0:
                raise EmployeeWageError("No companies registered yet!")
        except EmployeeWageError as e:
            print(str(e))
            self.main()        
        company_to_remove = input("Enter company name")
        try:
            self.company_list.remove([company for company in self.company_list if company.get_company_name() == company_to_remove][0] )
        except IndexError:
            print("Cannot delete! No such company registered.")
            self.main()    

    # prints all company from the list
    def print_companies(self):
        if(len(self.company_list)>0):
            print([company.get_company_name() for company in self.company_list])
        else:
            print("No companies registered yet! Please register first.")
            self.main()

employee = Employee()
employee.main()
