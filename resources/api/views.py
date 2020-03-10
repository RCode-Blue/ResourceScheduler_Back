from rest_framework import (
  viewsets, status
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from resources.models import Resource
from resources.api.serializers import (
  ResourceSerializer, ResourceSerializerPost)

@api_view(['GET', 'POST'])
def resources_list(request):
  if request.method == 'GET':
    if(request.data and request.data["organisation"]):
      org_id = request.data["organisation"]
      resources = Resource.objects.filter(organisation=org_id)
      serializer = ResourceSerializer(resources, many=True)
      return Response(serializer.data)

    resources = Resource.objects.all()
    serializer = ResourceSerializer(resources, many=True)
    return Response(serializer.data);

  elif request.method == 'POST':
    # print(request.data)
    serializer = ResourceSerializerPost(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def resource_detail(request, pk):
  try:
    resource = Resource.objects.get(pk=pk)
  except Resource.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = ResourceSerializer(resource)
    return Response(serializer.data)

  elif request.method == "PUT":
    serializer = ResourceSerializer(resource, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  elif request.method == "DELETE":
    resource.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

