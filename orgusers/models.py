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

# region (from tutorial)
  # _user = models.OneToOneField(
  #   User, 
  #   on_delete = models.CASCADE)
# endregion

  # region (from tutorial)
  # def __str__(self):
  #   return self._user.username
  # endregion