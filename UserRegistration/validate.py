import re
from abc import ABC, abstractmethod

class Validate(ABC):

    @abstractmethod
    def validate_input(self, user_input):
        pass

    def is_valid(self, pattern, user_input):
        match_object = re.match(pattern, user_input)
        return False if match_object == None else True