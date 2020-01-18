from rest_framework import viewsets

#region
# from rest_framework.generics import (
#   ListAPIView, 
#   RetrieveAPIView,
#   CreateAPIView,
#   UpdateAPIView,
#   DestroyAPIView
#   )
#endregion

from organisations.models import Organisation
from .serializers import OrganisationSerializer

class OrganisationViewSet(viewsets.ModelViewSet):
  serializer_class = OrganisationSerializer
  queryset = Organisation.objects.all()


#region
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
