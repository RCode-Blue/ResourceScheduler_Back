from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
  organisations_list,
  organisation_detail,
  organisations_list_filtered_out
)

urlpatterns = [
  path("org/", organisations_list),
  path("org/<int:pk>/", organisation_detail),
  # path("org/filtered/", organisations_list_filtered_out)
  path("org/filtered/", organisations_list_filtered_out)
]


urlpatterns = format_suffix_patterns(urlpatterns)






#region
# from rest_framework.routers import DefaultRouter

# from organisations.api.views import OrganisationViewSet

# router = DefaultRouter()
# router.register(r'org', OrganisationViewSet, basename='org')
# urlpatterns = router.urls
#endregion

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
