
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
  resources_list,
  resource_detail
)

urlpatterns = [
  path("resources/", resources_list),
  path("resources/<int:pk>/", resource_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)




#region
# from rest_framework.routers import DefaultRouter

# from .views import ResourceViewSet

# router = DefaultRouter()
# router.register(
#   r"resources", 
#   ResourceViewSet, 
#   basename="resources")
  
# urlpatterns = router.urls
#endregion