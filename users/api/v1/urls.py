from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GgjyuViewSet

router = DefaultRouter()
router.register("ggjyu", GgjyuViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
