from rest_framework.routers import DefaultRouter

from news.views import NewViewSet

router = DefaultRouter()

router.register(
    prefix='news', viewset=NewViewSet, basename='news'
)

urlpatterns = router.urls
