from rest_framework.routers import DefaultRouter
from api.views import AcaoViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'acoes', AcaoViewSet)

urlpatterns = router.urls