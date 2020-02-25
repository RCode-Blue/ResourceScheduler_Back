from django.db import models

# Create your models here.
class Organisation(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField(
    max_length=120,
    blank=True)
  address_line1 = models.CharField(
    max_length=120,
    blank=True)
  address_line2 = models.CharField(
    max_length=120,
    blank=True)
  suburb = models.CharField(
    max_length=80,
    blank=True)
  state = models.CharField(
    max_length=80,
    blank=True)
  postcode = models.CharField(
    max_length=18,
    blank=True)
  country = models.CharField(
    max_length=120,
    blank=True)
  logo = models.URLField(blank=True)

  def __str__(self):
    return self.name
    # return self.name(max_length=120)
