from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validateEmail(email:str):
    '''
    Return `True` for valid email id. \n
    Return `False` for invalid email id.
    '''
    try:
        validate_email(email)
        return True
    except ValidationError:
        print(f"{email} -- invalid email")
        return False