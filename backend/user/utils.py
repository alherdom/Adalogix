import random
import string
from email.mime.image import MIMEImage
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def password_generator(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def send_registration_email(firstname, lastname, mail, username, password):
    html_content = render_to_string(
        'password_mail.html',
        {
            'firstname': firstname,
            'lastname': lastname,
            'mail': mail,
            'username': username,
            'password': password,
        },
    )
    text_content = strip_tags(html_content)

    subject = 'Welcome to Adalogix! \U0001f44b'
    from_email = 'adalogixteam@gmail.com'
    to_email = mail
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')

    with open('user/templates/logo.png', 'rb') as f:
        image_data = f.read()
        msg_img = MIMEImage(image_data)
        msg_img.add_header('Content-ID', '<logo_image>')
        msg.attach(msg_img)
    msg.send()


def send_reset_password_email(firstname, lastname, mail, username, password):
    html_content = render_to_string(
        'reset_password_mail.html',
        {
            'firstname': firstname,
            'lastname': lastname,
            'mail': mail,
            'username': username,
            'password': password,
        },
    )
    text_content = strip_tags(html_content)

    subject = 'Password reset \U0001F513'  # Replace \U+1F513 with \U0001F513
    from_email = 'adalogixteam@gmail.com'
    to_email = mail
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')

    with open('user/templates/logo.png', 'rb') as f:
        image_data = f.read()
        msg_img = MIMEImage(image_data)
        msg_img.add_header('Content-ID', '<logo_image>')
        msg.attach(msg_img)
    msg.send()
