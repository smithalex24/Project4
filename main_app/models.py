from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
	destination = models.CharField(max_length=100)
	duration = models.CharField(max_length=100)
	languages = models.CharField(max_length=100)
	climate = models.CharField(max_length=100)
	items_needed = models.CharField(max_length=2000)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
	return self.name

