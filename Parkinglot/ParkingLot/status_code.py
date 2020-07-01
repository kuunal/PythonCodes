status_codes={
    200:"ok",
    201:"created",
    400:"Bad Request",
    401:"Unauthorized",
    403:"Forbidded",
    404:"page_not_found",
    500:"server_error"
}

def get_status_codes(id):
    for key, values in status_codes.items():
        if key == id:   
            return {key:values}