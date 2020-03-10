from django.db import models

from organisations.models import Organisation

class Resource(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField()
  organisation = models.ForeignKey(
    Organisation, 
    related_name="resources",
    on_delete=models.CASCADE)

  def __str__(self):
    # return self.name
    return (self.name + "-" + self.description)

