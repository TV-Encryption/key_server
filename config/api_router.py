from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from key_server.key_management_system.views import KeyViewSet
from key_server.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("keys", KeyViewSet)


app_name = "api"
urlpatterns = router.urls
