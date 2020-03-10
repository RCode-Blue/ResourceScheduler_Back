from django.db import models

from users.models import User
from organisations.models import Organisation

class OrgUser(models.Model):
  _user = models.ForeignKey(
    User, 
    related_name='_user',
    on_delete=models.CASCADE)

  
  organisation = models.ForeignKey(
    Organisation, 
    related_name='organisation',
    on_delete=models.CASCADE)

  job_title = models.TextField(
    max_length=120,
    blank=True)

  department = models.TextField(
    max_length=120,
    blank=True)

  is_admin = models.BooleanField()
  is_employee = models.BooleanField()

