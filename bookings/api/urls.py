from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
  bookings_list,
  booking_detail,
  bookings_by_resource
)

urlpatterns = [
  path("bookings/", bookings_list),
  path("bookings/<int:pk>/", booking_detail),
  path("bookings/filtered/<int:res_id>/", bookings_by_resource)
]

urlpatterns = format_suffix_patterns(urlpatterns)
