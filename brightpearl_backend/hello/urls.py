from rest_framework import routers
from .views import HelloViewSet

router = routers.SimpleRouter()

router.register(r'hello', HelloViewSet, base_name='hello')
urlpatterns = router.urls
