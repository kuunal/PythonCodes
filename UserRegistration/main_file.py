from registration_factory import RegistrationFactory


class MainClass:

    def get_input(self, input_type, input_data):
        factory = RegistrationFactory()
        obj = factory.return_object(input_type)
        return obj.validate_input(input_data)