from rest_framework import (
  viewsets, status
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from organisations.models import Organisation
from organisations.api.serializers import OrganisationSerializer

@api_view(["GET", "POST"])
def organisations_list(request):
  if request.method == "GET":
    organisations = Organisation.objects.all()
    serializer = OrganisationSerializer(organisations, many=True)
    return Response(serializer.data)

  elif request.method == "POST":
    serializer = OrganisationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def organisation_detail(request, pk):
  try:
    organisation = Organisation.objects.get(pk=pk)
  except Organisation.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = OrganisationSerializer(organisation)
    return Response(serializer.data)

  if request.method == "PUT":
    serializer = OrganisationSerializer(organisation, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  if request.method == "DELETE":
    organisation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
# Given an array of organisation ids, get the orgs that do not match
def organisations_list_filtered_out(request, **kwargs):
  if request.method == "GET":
    print("---------")
    print(request.data)
    orgs = Organisation.objects.exclude(id__in=request.data["org_ids"])
    serializer = OrganisationSerializer(orgs, many=True)
    return Response(serializer.data)
    # organisations = []
    # if(request.data and request.data["org_ids"]):
    #   for org_id in request.data["org_ids"]:
    #     org = Organisation.objects.get(id=org_id)
    #     serializer = OrganisationSerializer(org)
    #     organisations.append(serializer.data)
    #   return Response(organisations)


  








#region
# from rest_framework import viewsets

# from organisations.models import Organisation
# from .serializers import OrganisationSerializer

# class OrganisationViewSet(viewsets.ModelViewSet):
#   serializer_class = OrganisationSerializer
#   queryset = Organisation.objects.all()
#endregion

#region
# from rest_framework.generics import (
#   ListAPIView, 
#   RetrieveAPIView,
#   CreateAPIView,
#   UpdateAPIView,
#   DestroyAPIView
#   )

# class OrganisationListView(ListAPIView):
#   queryset = Organisation.objects.all()
#   serializer_class = OrganisationSerializer

# class OrganisationDetailView(RetrieveAPIView):
#   queryset = Organisation.objects.all()
#   serializer_class = OrganisationSerializer

# class OrganisationCreateView(CreateAPIView):
#   queryset = Organisation.objects.all()
#   serializer_class = OrganisationSerializer

# class OrganisationUpdateView(UpdateAPIView):
#   queryset = Organisation.objects.all()
#   serializer_class = OrganisationSerializer

# class OrganisationDeleteView(DestroyAPIView):
#   queryset = Organisation.objects.all()
#   serializer_class = OrganisationSerializer
#endregion
