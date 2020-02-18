from rest_framework import serializers

from organisations.models import Organisation
from resources.api.serializers import ResourceSerializer

class OrganisationSerializer(serializers.ModelSerializer):
  resources = ResourceSerializer(
    many=True, 
    read_only=True,
    required=False)

  class Meta:
    model = Organisation
    fields = (
      'id', 
      'name', 
      'description',
      'resources',
      'address_line1',
      'address_line2',
      'suburb',
      'state',
      'postcode',
      'country',
      'logo'
      )

# class OrganisationSerializerPost(serializers.ModelSerializer):



      