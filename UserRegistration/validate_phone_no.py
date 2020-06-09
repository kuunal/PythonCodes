from validate import Validate

class PhoneNumber(Validate):

    def validate_input(self, input_data):
        phone_number_pattern = "^[0-9]{2} [0-9]{10}$"
        return super().is_valid(phone_number_pattern, input_data)