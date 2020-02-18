from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
  orgusers_list,
  orguser_detail,
  orguser_by_userId,
  orguser_by_userId_test
)

urlpatterns = [
  path("orgusers/", orgusers_list),
  path("orgusers/<int:pk>/", orguser_detail),
  path("orgusers/user/<int:userid>/", orguser_by_userId),
  path("orgusers/user/test/", orguser_by_userId_test)
]

urlpatterns = format_suffix_patterns(urlpatterns)




#region (original)
# from rest_framework.routers import DefaultRouter

# from orgusers.api.views import OrgUserViewSet

# router = DefaultRouter()
# router.register(
#   r"orgusers",
#   OrgUserViewSet,
#   basename="orgusers")

# urlpatterns = router.urls
#endregion