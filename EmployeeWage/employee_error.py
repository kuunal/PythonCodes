class EmployeeWageError(Exception):
    def __init__(self,message="Somethinf went wrong"):
        super().__init__(message)
