from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  middle_name = models.CharField(
    max_length=120,
    blank=True,
    null=True)
  preferred_name = models.CharField(
    max_length=120,
    blank=True,
    null=True)
  dob = models.DateField(
    null=True)
  photo = models.URLField(
    blank=True,
    null=True)

  def __str__(self):
    return self.username