from ParkingLot.redis_setup import get_redis_instance
from main.jwt_decode import jwt_decode
from rest_framework import exceptions
from status_code import get_status_codes
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class LoginMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_request(request)
        return response

    def process_request(self, request):
        url_list = ['/register']
            
        redis_instance = get_redis_instance()
        try:
            token = request.headers.get('x_token')
            email = jwt_decode(token)
        except exceptions.AuthenticationFailed:
            return Response(get_status_codes(401))
        for key in redis_instance:
            if key.decode('utf-8') == email:
                request.data['logged_user'] = email
                print(request.data)
        return Response(get_status_codes(401))

    
