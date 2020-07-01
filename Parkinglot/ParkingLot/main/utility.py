# def is_authentic(token):
#     redis_instance = get_redis_instance()
#     for key in redis_instance.scan_iter():
#         if redis_instance.get(key).decode('utf-8') == token:
#             return key
#         return False
