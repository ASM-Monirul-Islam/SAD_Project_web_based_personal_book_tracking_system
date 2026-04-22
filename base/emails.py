from django.conf import settings
from django.core.mail import send_mail

def send_verification_mail(email, email_token):
	subject = "Verify Your Account at Goodreads"
	email_from = settings.EMAIL_HOST_USER
	message = (f"""
Hello,

You need to verify your account to login into GoodReads
			
Please click the link below to verify your account:
			
http://127.0.0.1:8000/activate/{email_token}

Thank you,

Goodreads""")
	send_mail(subject, message, email_from, [email])