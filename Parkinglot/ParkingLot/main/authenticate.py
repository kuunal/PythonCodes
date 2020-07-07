from rest_framework import permissions

class Autheticate(permissions.BasePermission):
    def is_authentic():
        redis_instance = get_redis_instance()
        print("assssssssssssssssssssss")
        for key in redis_instance.scan_iter():
            if key == None:
                return False
        return True