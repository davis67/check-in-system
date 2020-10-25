from django.contrib.auth.models import AbstractUser
from core import models as core_models
from django.db import models

class User(AbstractUser, core_models.TimeStampedModel):
	"""Custom user model """
	GENDER_MALE = "male"
	GENDER_FEMALE = "female"

	GENDER_CHOICES = (
		(GENDER_MALE, 'Male'),
		(GENDER_FEMALE, 'Female'),
	)

	avatar = models.ImageField(blank=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
	bio = models.TextField(blank=True)
	superhost = models.BooleanField(default=False)
