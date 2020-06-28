import re
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ResetSerializer(serializers.ModelSerializer):

    def validate_password(self, data):
        password = data
                # if password!=data['pass2']:
        #     raise ValidationError("Password and confirm dont match")
        if re.match("^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}",password):
            # self.set_password(password)
            # self.save()
            return super().validate(data)
        raise ValidationError("Please use numbers, symbols and Alphabets")  


    class Meta:
        model=User
        fields=['password']

        # self.set_password(request.data['password'])
    


