from validate import Validate

class Password(Validate):

    def validate_input(self, input_data):
        password_pattern = "^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}"
        return super().is_valid(password_pattern, input_data)