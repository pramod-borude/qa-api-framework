import random
import string

def random_username():
    return "user_" + "".join(random.choices(string.ascii_letters + string.digits, k=8))

def random_email():
    return "".join(random.choices(string.ascii_letters, k=6)) + "@mail.com"
