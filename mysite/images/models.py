from django.contrib.auth.models import User
from django.db import models

class images_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image=models.ImageField(null=True, blank=True)
