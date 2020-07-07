# from rest_framework import permissions
# from rest_framework.response import Response
# from django.shortcuts import redirect

# class Autheticate(object):
    
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         return self.get_response(request)

#     def process_request(self, request):        
#         redis_instance = get_redis_instance()
#         for key in redis_instance.scan_iter():
#             if key:
#                 return True
#         return redirect('login')