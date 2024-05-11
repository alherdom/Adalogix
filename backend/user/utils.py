import random
import string

def password_generator(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))