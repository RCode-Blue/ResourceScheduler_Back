from rest_framework import serializers

from resources.models import Resource
# from organisations.models import Organisation
# from organisations.api.serializers import OrganisationSerializer

class ResourceSerializer(serializers.ModelSerializer):
  org_name = serializers.CharField(
    read_only=True, 
    source="organisation.name",
    required=False)

  class Meta:
    model = Resource
    fields = (
      'id',
      "name",
      "description",
      "organisation",
      "org_name"
    )


class ResourceSerializerPost(serializers.ModelSerializer):
  class Meta:
    model = Resource
    fields = (
      'name', 'description', 'organisation'
    )



# class ResourceSerializerOrgName(serializers.ModelSerializer):
#   organisation = OrgNameSerializer()
#   class Meta:
#     model = Resource
#     fields = (
#       "name",
#       "description",
#       "organisation"
#     )