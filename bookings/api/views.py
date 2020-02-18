
# region (original)
# from rest_framework import viewsets

# from bookings.models import Booking
# from .serializers import BookingSerializer

# class BookingViewSet(viewsets.ModelViewSet):
#   serializer_class = BookingSerializer
#   queryset = Booking.objects.all()
# endregion


# region (new)
from rest_framework import (
  viewsets,
  status)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookings.models import Booking
from bookings.api.serializers import BookingSerializer
from resources.models import Resource
from resources.api.serializers import ResourceSerializer

# from django.http import JsonResponse

@api_view(['GET', 'POST'])
def bookings_list(request):
  if request.method == "GET":
    # print(request.data)

    if(request.data and request.data['resource_org_id']):
      org_id = request.data['resource_org_id']
      bookings = Booking.objects.filter(resource__organisation__id = org_id)
      serializer = BookingSerializer(bookings, many=True)
      return Response(serializer.data)

    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

  elif request.method == "POST":
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET", "PUT", "DELETE"])
def booking_detail(request, pk):
  try:
    booking = Booking.objects.get(pk=pk)
  except Booking.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = BookingSerializer(booking)
    return Response(serializer.data)

  elif request.method == "PUT":
    serializer = BookingSerializer(booking, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == "DELETE":
    booking.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(["GET"])
def bookings_by_resource(request, res_id):
  # print(request.json())
  if request.method == "GET":
    # print("-----")
    # print(res_id)
    # print(stuff)
    # print(request.data)
    
    # res_id = request.data["pk"]
    # print(res_id)
    # print("-----")

    bookings = Booking.objects.filter(resource = res_id)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # if(request.data):
      # today = datetime.date.today()
      # bookings = Booking.objects.filter(booking_start)

# endregion