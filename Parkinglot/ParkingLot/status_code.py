status_codes={
    200:"ok",
    400:"Invalid Email",
    401:"Invalid id or password",
    403:"please verify your email. Link has been sent to you!",
    404:"page_not_found",
    500:"server_error"
}

def get_status_codes(id):
    for key, values in status_codes.items():
        if key == id:   
            return {key:values}