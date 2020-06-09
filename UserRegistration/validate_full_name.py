from validate import Validate
import re

class FullName(Validate):

    def validate_input(self, user_input):
        full_name_pattern = "^[A-Z][a-z]{2,} [A-Z][a-z]{2,}$"
        return super().is_valid(full_name_pattern, user_input)