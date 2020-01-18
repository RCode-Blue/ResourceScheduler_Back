
from rest_framework.routers import DefaultRouter

from organisations.api.views import OrganisationViewSet

#region
# from django.urls import path

# from .views import (
#   OrganisationListView, 
#   OrganisationDetailView,
#   OrganisationCreateView,
#   OrganisationUpdateView,
#   OrganisationDeleteView
#   )

# urlpatterns = [
#   path('org/', OrganisationListView.as_view()),
#   path('org/neworg/', OrganisationCreateView.as_view()),
#   path('org/<pk>', OrganisationDetailView.as_view()),
#   path('org/<pk>/update/', OrganisationUpdateView.as_view()),
#   path('org/<pk>/del/', OrganisationDeleteView.as_view())
# ]
#endregion

router = DefaultRouter()
router.register(r'org', OrganisationViewSet, basename='org')
urlpatterns = router.urls
