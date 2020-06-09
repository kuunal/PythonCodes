from validate import Validate
import re

class Email(Validate):

    def validate_input(self, user_input):
        email_pattern = "^[a-zA-Z0-9]+[\\.\\-\\+\\_]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[.]?[a-zA-Z]{2,4}[\\.]?([a-z]{2,4})?$"
        return super().is_valid(email_pattern, user_input)
        