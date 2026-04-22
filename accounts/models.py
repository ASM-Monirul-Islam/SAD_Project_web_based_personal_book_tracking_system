from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from base.emails import send_verification_mail


class Profile(BaseModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=15, null=True, blank=True)
	is_email_verified = models.BooleanField(default=False)
	email_token = models.CharField(max_length=255, blank=True, null=True)
	image = models.ImageField(upload_to='profile/', null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	interests = models.TextField(null=True, blank=True)
	fav_quotes = models.TextField(null=True, blank=True)
 
@receiver(post_save, sender=User)
def email_token_sender(sender, instance, created, **kwargs):
	try:
		if created:
			email_token = str(uuid.uuid4())
			Profile.objects.create(user=instance, email_token=email_token)
			email = instance.email
			send_verification_mail(email, email_token)
	except Exception as e:
		print(e)