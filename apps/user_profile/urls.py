from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("users-read", viewset=views.UserViewSet, basename="users-read")
router.register("users", viewset=views.UserCreateViewSet)
router.register("profile", viewset=views.UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
