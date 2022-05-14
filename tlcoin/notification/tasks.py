import imp
import os
from datetime import datetime

from decouple import Csv, config

from .models import PriceThresholdNotifications
from .utilis import validate_email

LOWER_PRICE_LIMIT = config('MIN_PRICE_LIMIT', cast=int)
UPPER_PRICE_LIMIT = config('MAX_PRICE_LIMIT', cast=int)
USER_EMAIL = config('USER_EMAIL', cast=Csv())

def notifier(price, coin="bitcoin"):
    '''
    Method to trigger notification based on upper and lower price limit.
    '''
    if USER_EMAIL:
        email = USER_EMAIL[0] # for now, supports only one email
        subject, message, threshold_type = get_notification_info(email, price, coin)
        if subject and message:
            #TODO - SEND EMAIL
            
            update_notification_status(email, threshold_type, coin)
            print("****notification task completed****")
    else:
        print("No user for notification")

def get_notification_info(email, price, coin):
    if LOWER_PRICE_LIMIT:
        if price < LOWER_PRICE_LIMIT:
            threshold_type = "lower"
            allowed = check_notification_status(email, threshold_type, coin)
            if allowed:
                subject = f"{coin} is low"
                message = f"{coin.upper()} price is {price} USD."
                return subject, message, threshold_type

    if UPPER_PRICE_LIMIT:
        if price > UPPER_PRICE_LIMIT:
            threshold_type = "upper"
            allowed = check_notification_status(email, threshold_type, coin)
            if allowed:
                subject = f"{coin} is high"
                message = f"{coin.upper()} price is {price} USD."
                return subject, message, threshold_type

    return (None, None, None)

def check_notification_status(email, threshold_type, coin):
    '''
    Check if notification already sent to user for today. \n
    Return `True` if no notification sent to user for given limit and coin.
    '''
    today = datetime.today()
    if threshold_type == "lower":
        if not PriceThresholdNotifications.objects.filter(email=email, lower_threshold_flag=True, coin_id=coin, created_at__date=today):
            return True
    elif threshold_type == "upper":
        if not PriceThresholdNotifications.objects.filter(email=email, upper_threshold_flag=True, coin_id=coin, created_at__date=today):
            return True
    else:
        return False

def update_notification_status(email, threshold_type, coin):
    '''
    update the notification tracker for the day and given arguments.
    '''
    today = datetime.today()
    if threshold_type == "lower":
        lower_obj = PriceThresholdNotifications(email=email, lower_threshold_flag=True, coin_id=coin, created_at=today)
        lower_obj.save()
    elif threshold_type == "upper":
        higher_obj = PriceThresholdNotifications(email=email, upper_threshold_flag=True, coin_id=coin, created_at=today)
        higher_obj.save()



