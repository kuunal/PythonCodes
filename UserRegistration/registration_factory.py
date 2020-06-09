from validate_full_name import FullName
from validate_email import Email
from validate_phone_no import PhoneNumber
from validate_password import Password

class RegistrationFactory:

    def return_object(self, input_type):
        switcher = {
            "name" : FullName(),
            "email": Email(),
            "phone": PhoneNumber(),
            "password":Password()
        }
        return switcher.get(input_type)
 