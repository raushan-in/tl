from django.core.mail import send_mail
from .utilis import validateEmail

FROM_EMAIL = "raushan.kumar@gmail.com" 

def send_email(subject, message, to_list:list):
    valid_to = filter(validateEmail, to_list)
    return send_mail(subject, message, FROM_EMAIL, valid_to)