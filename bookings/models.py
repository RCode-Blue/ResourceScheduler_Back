from django.db import models

from resources.models import Resource
from orgusers.models import OrgUser

class Booking(models.Model):
  title = models.CharField(
    max_length=120
    )
  organizer = models.ForeignKey(
    OrgUser,
    default=1,
    related_name="organizer",
    on_delete=models.CASCADE
  )
  description = models.TextField(
    blank=True
    )
  resource = models.ForeignKey(
    Resource,
    related_name="resource",
    on_delete=models.CASCADE
  )
  booking_start = models.DateTimeField()
  booking_end = models.DateTimeField()


