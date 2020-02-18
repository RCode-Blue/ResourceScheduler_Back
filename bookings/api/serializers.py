from rest_framework import serializers

from bookings.models import Booking
from resources.api.serializers import ResourceSerializer

class BookingSerializer(serializers.ModelSerializer):
  resource_detail = ResourceSerializer(
    source="resource", read_only=True)


  resource_name = serializers.CharField(
    read_only=True, 
    source="resource.name",
    required=False)
  resource_description = serializers.CharField(
    read_only=True, 
    source="resource.description",
    required=False)
  resource_org_id = serializers.IntegerField(
    read_only=True,
    source="resource.organisation.id",
    required=False)
  resource_org_name = serializers.CharField(
    read_only=True, 
    source="resource.org_name",
    required=False)
  

  class Meta:
    model = Booking
    fields = (
      "id",
      "title",
      "description",
      "resource",
      "booking_start",
      "booking_end",

      "resource_detail",
      "resource_name",
      "resource_description",
      "resource_org_id",
      "resource_org_name"
    )