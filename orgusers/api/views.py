from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import parser_classes  #for testing
from rest_framework.parsers import JSONParser         # for testing


from orgusers.models import OrgUser
from .serializers import OrgUserSerializer, OrgUserSerializerDetails

@api_view(['GET', 'POST'])
def orgusers_list(request):
  if request.method == "GET":
    if(request.data and request.data['userid']):
      user_id = request.data['userid']
      orgusers = OrgUser.objects.filter(_user__id = user_id)
      print(orgusers)
      serializer = OrgUserSerializerDetails(orgusers, many=True)
      return Response(serializer.data)
    orgusers = OrgUser.objects.all()
    serializer = OrgUserSerializerDetails(orgusers, many=True)
    return Response(serializer.data)

  elif request.method == "POST":
    serializer = OrgUserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def orguser_detail(request, pk):
  try:
    orguser = OrgUser.objects.get(pk=pk)
  except OrgUser.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = OrgUserSerializer(orguser)
    return Response(serializer.data)

  elif request.method == "PUT":
    serializer = OrgUserSerializer(orguser, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == "DELETE":
    orguser.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def orguser_by_userId(request, userid):
  if request.method == "GET":
    orgusers = OrgUser.objects.filter(_user__id = userid)
    serializer = OrgUserSerializerDetails(orgusers, many=True)
    return Response(serializer.data)


# for testing
@api_view(["GET"])
@parser_classes([JSONParser])
def orguser_by_userId_test(request):
  if request.method == "GET":
    userid=request.data["userid"]
    orgusers = OrgUser.objects.filter(_user__id = userid)
    serializer = OrgUserSerializerDetails(orgusers, many=True)
    return Response(serializer.data)