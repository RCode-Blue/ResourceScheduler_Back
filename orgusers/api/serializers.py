from rest_framework import serializers

from orgusers.models import OrgUser
from organisations.models import Organisation
from organisations.api.serializers import OrganisationSerializer
from users.models import User
from users.api.serializers import UserSerializer

class OrgUserSerializer(serializers.ModelSerializer):
  organisation = serializers.PrimaryKeyRelatedField(
    queryset=Organisation.objects.all(),
    required=True
  )

  # _user_details = UserSerializer()

  _user = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    required=True
  )

  class Meta:
    model = OrgUser
    fields = (
      "id",
      "_user",
      "organisation",
      "is_admin",
      "is_employee",
      "job_title",
      "department"
    )

class OrgUserSerializerDetails(serializers.ModelSerializer):
  organisation = OrganisationSerializer()
  _user = UserSerializer()


  class Meta:
    model = OrgUser
    fields = (
      "id",
      "_user",
      "organisation",
      "is_admin",
      "is_employee",
      "job_title",
      "department"
    )
