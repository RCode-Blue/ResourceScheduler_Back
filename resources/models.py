from django.db import models

from organisations.models import Organisation

class Resource(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField()
  organisation = models.ForeignKey(
    Organisation, 
    related_name="resources",
    on_delete=models.CASCADE)

# region
  # def __str__(self):
  #   return '{ "name" : %s, "description": %s }' % (self.name, self.description)
    # response = "{" + '"name"' + ":" + '"' + self.name + '"' + "," + '"description"' + ":" + '"' + self.description + '"' + "}"
    # return response
#endregion
